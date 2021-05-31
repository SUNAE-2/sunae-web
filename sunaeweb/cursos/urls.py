from django.urls import path

from . import views

urlpatterns = [
    path('', views.course, name='cursos'),
    path('config/', views.stripe_config),
    path('create-checkout-session/<name>/<price>', views.create_checkout_session),
]