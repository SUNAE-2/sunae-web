from carreras.models import Carrera
from django.db import models

# Create your models here.
class Asesorias(models.Model):
    fullname = models.CharField(max_length=20)
    description = models.TextField()
    email = models.EmailField()
    carrera= models.ForeignKey(Carrera, on_delete= models.CASCADE)
    active = models.BooleanField()
    def __str__(self):
        return self.fullname


