from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio-details/', views.portfolio, name='portfolio-details'),
]