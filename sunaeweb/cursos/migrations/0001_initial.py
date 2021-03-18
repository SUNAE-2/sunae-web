# Generated by Django 2.2.12 on 2021-03-07 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=100)),
                ('fechaInicio', models.DateField()),
                ('fechaFinal', models.DateField()),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
    ]