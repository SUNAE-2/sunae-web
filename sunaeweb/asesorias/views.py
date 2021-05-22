from django.shortcuts import render, redirect
from carreras.models import Carrera
from cursos.models import Curso
from .forms import *


# Create your views here.
def asesorias(request, *args, **kwargs):
    obj = Carrera.objects.filter(activo__exact=True)
    cursos = Curso.objects.filter(activo__exact=True)
    if request.method == 'POST':
        form = AsesoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucess')
    else:
        form = AsesoriaForm()
    context = {
        'object': obj,
        'courses': cursos,
        'form': form,
    }
    return render(request, 'asesorias.html', context=context)


def success(request, *args, **kwargs):
    obj = Carrera.objects.filter(activo__exact=True)
    cursos = Curso.objects.filter(activo__exact=True)
    context = {
        'object': obj,
        'courses': cursos,
    }
    return render(request, 'contact_sucess.html', context=context)