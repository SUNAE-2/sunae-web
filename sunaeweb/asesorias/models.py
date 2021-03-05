from django.db import models
from carreras.models import Carrera

class Asesorias(models.Model):
    alumno = models.CharField(max_length=20)
    description = models.TextField()
    correo = models.EmailField()
    carrera= models.ForeignKey(Carrera, on_delete= models.CASCADE)
    activo = models.BooleanField()