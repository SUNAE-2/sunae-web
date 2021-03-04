from django.db import models

# Create your models here.

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=1000)
    respuesta = models.CharField(max_length=1000)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.pregunta