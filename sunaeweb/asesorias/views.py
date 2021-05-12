from django.shortcuts import render, redirect
from carreras.models import *
from .forms import *


# Create your views here.
def asesorias(request, *args, **kwargs):
    if request.method == 'POST':
        form = AsesoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucess')
    else:
        form = AsesoriaForm()
    return render(request, 'asesorias.html', {'form': form})


def sucess(request):
    return render(request, 'contact_sucess.html', {})