# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-22 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default=b'', max_length=100, verbose_name=b'Nombre')),
                ('descripcion', models.TextField(blank=True, default=b'', null=True, verbose_name=b'Descripci\xc3\xb3n')),
                ('codigo', models.CharField(blank=True, max_length=10, null=True, verbose_name=b'C\xc3\xb3digo')),
                ('facultad', models.CharField(blank=True, choices=[(0, b'Facultad de Sistemas'), (1, b'Facultad de Industrial'), (2, b'Facultad de Civil'), (3, b'Facultad de El\xc3\xa9ctrica')], default=0, max_length=30, null=True, verbose_name=b'G\xc3\xa9nero')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de creaci\xc3\xb3n')),
                ('fecha_de_actualizacion', models.DateTimeField(auto_now=True, verbose_name=b'Fecha de actualizaci\xc3\xb3n')),
            ],
            options={
                'ordering': ['facultad', 'nombre'],
                'db_table': 'asignaturas',
                'verbose_name_plural': 'Asignaturas',
            },
        ),
        migrations.AlterModelOptions(
            name='estudiante',
            options={'ordering': ['nombre'], 'verbose_name_plural': 'Estudiantes'},
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='genero',
            field=models.CharField(blank=True, choices=[(b'hombre', b'Hombre'), (b'mujer', b'Mujer'), (b'otros', b'Otros')], default=b'otros', max_length=30, null=True, verbose_name=b'G\xc3\xa9nero'),
        ),
    ]