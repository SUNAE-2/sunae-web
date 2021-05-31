from django.shortcuts import render
from .models import Curso, Carrera
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import stripe

def course(request, *args, **kwargs):
    obj = Carrera.objects.filter(activo__exact=True)
    cursos = Curso.objects.filter(activo__exact=True)
    context = {
        'courses': cursos,
        'object': obj,
    }
    return render(request, 'courses.html', context=context)

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request, name, price):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                allow_promotion_codes=True,
                line_items=[
                    {
                        'name': name,
                        'quantity': 1,
                        'currency': 'mxn',
                        'amount': price+'00',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})