# Generated by Django 2.2.12 on 2021-03-07 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=1000)),
                ('respuesta', models.CharField(max_length=1000)),
                ('activa', models.BooleanField(default=True)),
            ],
        ),
    ]
