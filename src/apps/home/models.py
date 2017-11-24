# -*- coding: utf-8 -*-
"""
Models.py
"""
from django.db import models
from django.utils.text import slugify

# from src.apps.core.models import BaseModel
# from src.apps.users.models import User


class Contact(models.Model):
    """Contact model"""
    email = models.CharField(max_length=100, blank=False, null=False, default='', verbose_name='Correo')
    subject = models.CharField(max_length=255, blank=True, null=True, default='', verbose_name='Asunto')
    message = models.TextField(blank=True, null=True, default='', verbose_name='Mensaje')
    # user = models.ForeignKey(User, default=None, blank=True, verbose_name='Usuario')

    class Meta:
        verbose_name_plural = 'Contactos'
        db_table = 'contact'
        ordering = ['-subject', '-message']

    def __unicode__(self, *args, **kwargs):
        return '{}'.format(self.subject)

    def __str__(self, *args, **kwargs):
        return '{} - {}'.format(self.email, self.subject)


class Estudiante(models.Model):
    HOMBRE = 'hombre'
    MUJER = 'mujer'
    OTROS = 'otros'

    GENRE_CHOICES = (
        (HOMBRE, "Hombre"),
        (MUJER, "Mujer"),
        (OTROS, "Otros"),
    )

    slug = models.SlugField(max_length=100, unique=True, blank=False, null=False, default='', verbose_name='Slug')

    nombre = models.CharField(max_length=100, blank=False, null=False, default='', verbose_name='Nombre')
    apellido = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name='Apellido')
    edad = models.PositiveIntegerField(blank=True, null=True, verbose_name='Edad')
    genero = models.CharField(max_length=30, choices=GENRE_CHOICES, default=OTROS,
                              blank=True, null=True, verbose_name='Género')
    salario = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True,
                                  verbose_name='Salario')

    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_de_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name_plural = 'Estudiantes'
        db_table = 'estudiantes'
        ordering = ['nombre', ]

    def __unicode__(self, *args, **kwargs):
        # Python 2
        return '{}'.format(self.nombre)

    def __str__(self, *args, **kwargs):
        # Python 3
        ctx = {
            'nombre': self.nombre,
            'apellido': self.apellido
        }
        return '{nombre} - {apellido}'.format(**ctx)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Estudiante, self).save(*args, **kwargs)


class Asignatura(models.Model):
    SISTEMAS = '0'
    INDUSTRIAL = '1'
    CIVIL = '2'
    ELECTRICA = '3'

    FACULTY_CHOICES = (
        (SISTEMAS, "Facultad de Sistemas"),
        (INDUSTRIAL, "Facultad de Industrial"),
        (CIVIL, "Facultad de Civil"),
        (ELECTRICA, "Facultad de Eléctrica"),
    )

    slug = models.SlugField(max_length=100, unique=False, blank=False, null=False, default='', verbose_name='Slug')

    nombre = models.CharField(max_length=100, blank=False, null=False, default='', verbose_name='Nombre')
    descripcion = models.TextField(blank=True, null=True, default='', verbose_name='Descripción')
    codigo = models.CharField(max_length=10, blank=True, null=True, verbose_name='Código')
    facultad = models.CharField(max_length=30, choices=FACULTY_CHOICES, default=SISTEMAS,
                                blank=True, null=True, verbose_name='Género')

    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    fecha_de_actualizacion = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name_plural = 'Asignaturas'
        db_table = 'asignaturas'
        ordering = ['facultad', 'nombre', ]

    def __unicode__(self, *args, **kwargs):
        # Python 2
        return '{}'.format(self.nombre)

    def __str__(self, *args, **kwargs):
        # Python 3
        return '{} - {}'.format(self.facultad, self.nombre)
