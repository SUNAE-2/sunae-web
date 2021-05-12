from django.urls import path

from . import views

urlpatterns = [
    path('', views.asesorias, name='asesorias'),
    path('sucess', views.sucess, name='sucess')
]