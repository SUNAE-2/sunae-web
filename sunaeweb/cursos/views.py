from django.shortcuts import render
from .models import Curso

def course(request, *args, **kwargs):
    cursos = Curso.objects.filter(activo__exact=True)
    context = {
        'courses': cursos
    }
    return render(request, 'courses.html', context=context)