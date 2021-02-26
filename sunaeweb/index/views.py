from django.shortcuts import render

# Create your views here.
def home(request, *args, **kwargs):
    return render(request, 'home.html', {})

def faq(request, *args, **kwargs):
    return render(request, 'faq.html')

def portfolio(request, *args, **kwargs):
    return render(request, 'portfolio-details.html')

def inner_page(request, *args, **kwargs):
    return render(request, 'inner-page.html', {})
