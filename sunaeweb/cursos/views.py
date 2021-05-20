from django.shortcuts import render
from .models import Curso, Carrera

def course(request, *args, **kwargs):
    obj = Carrera.objects.filter(activo__exact=True)
    cursos = Curso.objects.filter(activo__exact=True)
    context = {
        'courses': cursos,
        'object': obj,
    }
    return render(request, 'courses.html', context=context)