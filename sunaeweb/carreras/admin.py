from django.contrib import admin

from .models import Carrera, Instructor, Coordinador

# Register your models here.
admin.site.register(Carrera)
admin.site.register(Instructor)
admin.site.register(Coordinador)