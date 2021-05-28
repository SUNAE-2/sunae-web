from django.db import models
from django.db.models.signals import post_save
from carreras.models import Carrera
from django.dispatch import receiver

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

class Prepa(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class Uni(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre

class Inscrito(models.Model):
    curso = models.ForeignKey(Curso, on_delete= models.CASCADE)
    nombre = models.CharField(max_length=200)
    correo = models.EmailField(max_length=254)
    telefono = models.IntegerField()
    prepa = models.ForeignKey(Prepa, on_delete= models.CASCADE)
    uni = models.ForeignKey(Uni, on_delete= models.CASCADE)
    carrera = models.CharField(max_length=200)
    semestre = models.IntegerField()
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre + ' - ' + self.curso

@receiver(post_save, sender=Curso)
def cursoInactivo(sender, instance, created, **kwargs):
    if not created:
        ac = instance.activo
        Inscrito.objects.filter(curso=instance).update(activo=ac)
    

