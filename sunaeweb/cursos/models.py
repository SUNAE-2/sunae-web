from django.db import models
from carreras.models import Carrera

class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    carrera= models.ForeignKey(Carrera, on_delete= models.CASCADE)
    descripcion = models.CharField(max_length=100)
    fechaInicio = models.DateField()
    fechaFinal = models.DateField()
    precio = models.FloatField(default=0)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre