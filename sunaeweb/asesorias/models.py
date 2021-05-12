from django.db import models
from carreras.models import Carrera

class Asesoria(models.Model):
    alumno = models.CharField(max_length=50)
    description = models.TextField()
    correo = models.EmailField()
    carrera= models.ForeignKey(Carrera, on_delete= models.CASCADE)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return str(self.carrera) + " " + self.alumno
