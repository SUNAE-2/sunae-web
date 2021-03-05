from django.db import models

class Cursos(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=100)
    fechaInicio = models.DateField()
    fechaFinal = models.DateField()
    activo = models.BooleanField(default=True)