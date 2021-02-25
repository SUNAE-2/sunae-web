from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('faq', views.faq, name='faq'),
    path('portfolio-details/', views.portfolio, name='portfolio-details'),
]