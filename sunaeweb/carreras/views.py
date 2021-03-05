from django.shortcuts import render

from .models import Carrera

def carreras(request, *args, **kwargs):
    carre = Carrera.objects.filter(activo__exact=True)
    context = {
        'carre': carre
    }
    return render(request, 'home.html', context=context)