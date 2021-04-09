from django.urls import path

from . import views

app_name = ''
urlpatterns = [
    path('', views.home, name='index'),
    path('<int:id>/', views.carrera, name='carrera'),
    path('faq', views.faq, name='faq'),
    # path('portfolio-details/', views.portfolio, name='portfolio-details'),
    # path('inner-page/', views.inner_page, name='inner-page'),
    path('admin/reporte', views.reports, name='report'),
]