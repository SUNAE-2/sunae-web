from django.urls import path

from . import views

urlpatterns = [
    path('', views.asesorias, name='asesorias')
]