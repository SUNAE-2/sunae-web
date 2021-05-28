from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

    
class Carrera(models.Model):
    nombre = models.CharField(max_length=20, unique=True)
    descripcion = models.TextField()
    imagen = models.ImageField(default=None, upload_to='assets/img/carreras', null=True, blank=True)
    activo = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('carrera', kwargs={'nombre': self.nombre})

    def __str__(self):
        return self.nombre


class Instructor(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    materia = models.CharField(max_length=40, null=True)
    correo = models.EmailField()
    descripcion = models.TextField(default="")
    imagen = models.ImageField(default=None, upload_to='assets/img/instructores', blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Coordinador(models.Model):
    carrera = models.OneToOneField(Carrera, on_delete=models.CASCADE)
    coordinador = models.OneToOneField(Instructor, on_delete=models.CASCADE)
    imagen = models.ImageField(default=None, upload_to='assets/img/coordinadores', null=True, blank=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.carrera.nombre + " - " + self.coordinador.nombre

@receiver(post_save, sender=Carrera)
def carreraInactiva(sender, instance, created, **kwargs):
    if not created:
        ac = instance.activo
        Instructor.objects.filter(carrera=instance).update(activo=ac)
        Coordinador.objects.filter(carrera=instance).update(activo=ac)