from django import forms
from django.forms import *
from django.http import HttpResponse, BadHeaderError, HttpResponseRedirect
from django.core.mail import send_mail
from carreras.models import *
from asesorias.models import *
from django.db import models
from django.utils.translation import gettext_lazy as _


class Actions(models.IntegerChoices):
	COMPLETAR = 1, _('Marcar como completadas')
	RENVIAR = 2, _('Reenvíar correo a coordinador')


class AsesoriasManageForm(forms.Form):
	empty = [('', '----------------------')]
	action = ChoiceField(choices=empty + Actions.choices, label="Acción")

	def __init__(self, queryset):
		super(AsesoriasManageForm, self).__init__()
		self.fields['asesorias'] = IntegerField(
			widget=CheckboxSelectMultiple(choices=[(x.id, x.alumno) for x in queryset]))

