from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo': 'bienvenido a sunae'
    }
    return render(request, 'index.html', context=context)