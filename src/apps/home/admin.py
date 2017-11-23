# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Contact, Estudiante, Asignatura


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fields = ('email', 'subject', 'message')
    list_display = ('email', 'subject')
    search_fields = ['email', ]


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad', 'genero')
    list_filter = ('edad', 'genero')
    exclude = ('slug', )


@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'fecha_de_creacion')
    list_filter = ('facultad', 'nombre')
