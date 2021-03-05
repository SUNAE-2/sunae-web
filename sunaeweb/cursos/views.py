from django.shortcuts import render
from .models import Course

def course(request, *args, **kwargs):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses.html', context=context)