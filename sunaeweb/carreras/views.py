from django.shortcuts import render, get_object_or_404

from .models import Carrera, Instructor

def carrera(request, id):
    obj = get_object_or_404(Carrera, id=id)
    inst = Instructor.objects.filter(carrera=id)

    context = {
        'object': obj,
        'instructor': inst
    }
    return render(request, 'carrera.html', context=context)