from django.shortcuts import render, get_object_or_404

from .models import Carrera, Instructor

def carrera(request, nombre):
    obj = get_object_or_404(Carrera, nombre=nombre)
    inst = Instructor.objects.filter(carrera=obj)

    context = {
        'object': obj,
        'instructor': inst
    }
    return render(request, 'carrera.html', context=context)