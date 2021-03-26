from django.urls import path

from . import views

urlpatterns = [
    path('', views.carreras, name='carreras'), 
    path('/<int:id>/', views.carrera, name='carrera')
]