from django.contrib import admin

from .models import Carrera, Instructor

# Register your models here.
admin.site.register(Carrera)
admin.site.register(Instructor)