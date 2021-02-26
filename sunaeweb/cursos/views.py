from django.shortcuts import render

# Create your views here.

def cursos(request, *args, **kwargs):
    return render(request, 'home.html', {})