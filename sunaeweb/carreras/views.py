from django.shortcuts import render

# Create your views here.

def carreras(request, *args, **kwargs):
    return render(request, 'home.html', {})