from django.shortcuts import render
from .models import Cursos

def course(request, *args, **kwargs):
    cursos = Cursos.objects.filter(activo__exact=True)
    context = {
        'courses': cursos
    }
    return render(request, 'courses.html', context=context)