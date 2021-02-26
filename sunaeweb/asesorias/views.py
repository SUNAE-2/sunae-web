from django.shortcuts import render

# Create your views here.
def asesorias(request, *args, **kwargs):
    return render(request, 'home.html', {})