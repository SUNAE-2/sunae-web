from django import forms
from django.http import HttpResponse, BadHeaderError, HttpResponseRedirect
from django.core.mail import send_mail
from carreras.models import *
from asesorias.models import Asesoria


class AsesoriaForm(forms.Form):
    alumno = forms.CharField(max_length=50, label="",
                             widget=forms.TextInput(attrs={'placeholder': 'Nombre Completo'}))
    correo = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    descripcion = forms.CharField(max_length=250, label="",
                                  widget=forms.TextInput(attrs={'placeholder': 'Descripción del problema'}))
    carrera = forms.ModelChoiceField(queryset=Carrera.objects.all(), empty_label="Carrera", label="")

    def save(self):
        data = self.cleaned_data
        asesoria = Asesoria.objects.create(alumno=data['alumno'], description=data['descripcion'],
                                           correo=data['correo'], carrera=data['carrera'])
        mail = send_mail(subject="Asesoría " + data['alumno'], message=data['descripcion'], from_email="prueba@localhost.com",
                  recipient_list=[Coordinador.objects.get(carrera=data['carrera']).coordinador.correo])
        return asesoria if mail else None

