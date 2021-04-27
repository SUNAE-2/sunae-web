from django.urls import path

from . import views

app_name = ''
urlpatterns = [
    path('<int:id>/', views.carrera, name='carrera')
]