from django.core.mail import send_mail
from django.db import models
from carreras.models import Coordinador
def send_email(request):
    carrera = request.POST.get('carrera', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    coordinador = Coordinador.objects.get(Carrera__exact=carrera)
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')
)

