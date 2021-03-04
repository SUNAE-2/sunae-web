from django.shortcuts import render
from .models import Pregunta

# Create your views here.
def home(request, *args, **kwargs):
    return render(request, 'home.html', {})

def faq(request, *args, **kwargs):
    ques = Pregunta.objects.filter(activa__exact=True)
    context = {
        'ques': ques
    }
    return render(request, 'faq.html', context=context)

def portfolio(request, *args, **kwargs):
    return render(request, 'portfolio-details.html')

def inner_page(request, *args, **kwargs):
    return render(request, 'inner-page.html', {})


