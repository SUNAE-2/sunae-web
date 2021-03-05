from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    dateOn = models.DateField()
    dateOff = models.DateField()
    isActive = models.BooleanField(default=False)