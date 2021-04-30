from django.urls import path

from . import views

app_name = ''
urlpatterns = [
    path('<str:nombre>/', views.carrera, name='carrera')
]