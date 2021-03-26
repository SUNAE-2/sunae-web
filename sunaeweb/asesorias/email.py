from django.http import HttpResponse, BadHeaderError, HttpResponseRedirect
from django.core.mail import send_mail
from django.db import models
from carreras.models import Coordinador
from .models import Asesoria
def send_email(request):
    name = request.POST.get('name', '')
    carrera = request.POST.get('carrera', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    subject = request.POST.get('subject', '')
    nueva = Asesoria(alumno=name, description=message, correo=from_email, carrera=carrera)
    nueva.save()
    coordinador = Coordinador.objects.get(Carrera__exact=carrera)
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')

