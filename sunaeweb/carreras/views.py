from django.shortcuts import render, get_object_or_404

from .models import Carrera, Instructor
from cursos.models import Curso

def carrera(request, nombre):
    obj = Carrera.objects.filter(activo__exact=True)
    cursos = Curso.objects.filter(activo__exact=True)
    carre = get_object_or_404(Carrera, nombre=nombre)
    inst = Instructor.objects.filter(carrera=carre)
    context = {
        'object': obj,
        'courses': cursos,
        'carrera': carre,
        'instructor': inst
    }
    return render(request, 'carrera.html', context=context)