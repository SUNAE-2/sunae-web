from django.shortcuts import render, get_object_or_404

from .models import Carrera, Instructor

# def carrera(request, id):
#     carre = Carrera.objects.get(id=id)
#     # instr = Instructor.objects.filter(carre.nombre)
#     context = {
#         'carrera': carre,
#         'instructor': instr
#     }
#     return render(request, 'carrera.html', context=context)

def carrera(request, id):
    obj = get_object_or_404(Carrera, id=id) 
    context = {
        'object': obj
    }
    return render(request, 'carrera.html', context=context)