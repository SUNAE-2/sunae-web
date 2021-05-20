from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Pregunta
from .forms import *
from asesorias.models import Asesoria
from django.utils import timezone
from carreras.models import Carrera
import django.apps


# Create your views here.
def home(request, *args, **kwargs):
	obj = Carrera.objects.filter(activo__exact=True)
	context = {
		'object': obj
	}
	return render(request, 'home.html', context=context)


# def portfolio(request, *args, **kwargs):
#     return render(request, 'portfolio-details.html', {})


# def inner_page(request, *args, **kwargs):
#     return render(request, 'inner-page.html', {})


def faq(request, *args, **kwargs):
    ques = Pregunta.objects.filter(activa__exact=True)
    obj = Carrera.objects.filter(activo__exact=True)
    context = {
		'ques': ques,
        'object': obj
	}
    return render(request, 'faq.html', context=context)


##########ERROR HANDLERS#############
def handler404(request, *args, **argv):
    obj = Carrera.objects.filter(activo__exact=True)
    context = {
        'object': obj
    }
    return render(request, 'error404.html', context=context)


def handler500(request, *args, **argv):
    obj = Carrera.objects.filter(activo__exact=True)
    context = {
        'object': obj
    }
    return render(request, 'error404.html', context=context)


def filterModels(allowed, all):
	filtered = []
	for gen_class in all:
		for a in allowed:
			if a in str(gen_class):
				filtered.append(gen_class)
				break
	return filtered


@login_required(login_url="/admin/login/")
def reports(request, *args, **kwargs):
	allowed_classname = ["Carrera", "Instructor", "Coordinador", "Curso", "Asesoria"]
	models_class = filterModels(allowed_classname, django.apps.apps.get_models())
	models = []
	for c in models_class:
		d = {'name': c.__name__,
			'headings': [field.name for field in filter(lambda x: not 'Rel' in str(x), c._meta.get_fields())]}
		d['rows'] = list(map(lambda tuple: [getattr(tuple, field) for field in d['headings']], c.objects.all()))
		models.append(d)
	context = {
		'date': timezone.now().date(),
		'models': models
	}
	return render(request, 'admin/reporte.html', context)


@login_required(login_url="/admin/login/")
def asesorias_manage(request):
	if request.method == 'POST':
		action = int(request.POST['action'][0])
		objs = list(map(lambda x: int(x), request.POST.getlist('asesorias')))
		if action == 1:
			mark_complete(objs)
		elif action == 2:
			resend_email(objs)
	groups_carreras = Asesoria.objects.all().values('carrera__nombre').distinct()
	carreras = []
	for carrera in groups_carreras:
		name = carrera['carrera__nombre']
		asesorias = Asesoria.objects.filter(carrera__nombre=name, activo=True)
		form = AsesoriasManageForm(queryset=asesorias)
		carreras.append({
			'name': name,
			'form': form
		})
		context = {'carreras': carreras}
	return render(request, 'admin/asesorias_manage.html', context)


def resend_email(asesorias):
	for asesoria_id in asesorias:
		asesoria = Asesoria.objects.get(id=asesoria_id)
		send_mail(subject="Asesoría " + asesoria.alumno, message=asesoria.description, from_email="prueba@localhost.com",
				recipient_list=[Coordinador.objects.get(carrera=asesoria.carrera).coordinador.correo])


def mark_complete(asesorias):
	for asesoria_id in asesorias:
		asesoria = Asesoria.objects.get(id=asesoria_id)
		asesoria.activo = False
		asesoria.save()