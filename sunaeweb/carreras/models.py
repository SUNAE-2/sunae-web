from django.db import models

class Carrera(models.Model):
    carreer = models.CharField(max_length=20)
    instructor = models.TextField()
    correo = models.TextField()
    active = models.BooleanField()

    def __str__(self):
        return self.carreer