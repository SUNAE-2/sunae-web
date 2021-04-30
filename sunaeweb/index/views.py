from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pregunta
from asesorias.models import Asesoria
from django.utils import timezone
from carreras.models import Carrera
import django.apps


# Create your views here.
def home(request, *args, **kwargs):
    carre = Carrera.objects.filter(activo__exact=True)
    context = {
        'carre': carre
    }
    return render(request, 'home.html', context=context)
    #return render(request, 'error404.html', context=context)


def faq(request, *args, **kwargs):
    ques = Pregunta.objects.filter(activa__exact=True)
    context = {
        'ques': ques
    }
    return render(request, 'faq.html', context=context)

##########ERROR HANDLERS#############
def handler404(request, *args, **argv):
    return render(request, 'error404.html')

def handler500(request, *args, **argv):
    return render(request, 'error404.html')

# def portfolio(request, *args, **kwargs):
#     return render(request, 'portfolio-details.html', {})


# def inner_page(request, *args, **kwargs):
#     return render(request, 'inner-page.html', {})


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


