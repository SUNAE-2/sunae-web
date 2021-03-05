from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.TextField()
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre


class Instructor(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    activo = models.BooleanField()

    def __str__(self):
        return self.nombre


