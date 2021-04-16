from django.db import models
from django.urls import reverse

class Carrera(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()
    activo = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('carrera', kwargs={'id': self.id})

    def __str__(self):
        return self.nombre
    
class Instructor(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    correo = models.EmailField()
    activo = models.BooleanField(default=True)
    descripcion = models.TextField(default="")
    imagen = models.ImageField(default=None)

    def __str__(self):
        return self.nombre

class Coordinador(models.Model):
    carrera = models.OneToOneField(Carrera, on_delete=models.CASCADE)
    coordinador = models.OneToOneField(Instructor, on_delete=models.CASCADE)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.carrera.nombre + " - " + self.coordinador.nombre