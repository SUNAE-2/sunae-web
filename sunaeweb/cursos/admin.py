from django.contrib import admin

from .models import Curso, Prepa, Uni, Inscrito

admin.site.register(Curso)
admin.site.register(Prepa)
admin.site.register(Uni)
admin.site.register(Inscrito)