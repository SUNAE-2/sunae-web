from django.shortcuts import render

from .models import Carrera, Instructor

def carreras(request, *args, **kwargs):
    carre = Carrera.objects.filter(activo__exact=True)
    context = {
        'carre': carre
    }
    return render(request, 'home.html', context=context)

def carrera(request, id):
    carre = Carrera.objects.get(id=id)
    instr = Instructor.objects.filter(carre.nombre)
    context = {
        'carrera': carre,
        'instructor': instr
    }
    return render(request, 'carrera.html', context=context)
