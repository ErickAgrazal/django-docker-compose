# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView

from .forms import EstudianteModelForm, AsignaturaModelForm
from .models import Estudiante, Asignatura


class Ejercicios(TemplateView):
    def get_template(self, t, n):
        _t = ['attributes', 'headings']
        _n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        if str(t) not in _t:
            raise Exception('Not in the whitelist')

        if str(n) not in _n:
            raise Exception('Not in the whitelist')

        return '{0}/{1}'.format(t, n)

    def get(self, request, *args, **kwargs):
        template_name = self.get_template(self.kwargs.get('t'), self.kwargs.get('n'))
        return render(request, template_name)


class HomeView(TemplateView):
    template_name = "home.html"


class EstudianteListView(ListView):
    template_name = "estudiante_list.html"
    model = Estudiante
    http_method_names = [u'get', ]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter()


class EstudianteCreateView(CreateView):
    template_name = "estudiante_create.html"
    http_method_names = [u'get', u'post', ]
    success_url = '/estudiantes'
    form_class = EstudianteModelForm


class EstudianteUpdateView(UpdateView):
    template_name = "estudiante_create.html"
    http_method_names = [u'get', u'post', ]
    success_url = '/estudiantes'
    form_class = EstudianteModelForm
    model = Estudiante


class EstudianteDeleteView(DeleteView):
    template_name = "estudiante_delete.html"
    model = Estudiante
    success_url = '/estudiantes'


class AsignaturaListView(ListView):
    template_name = "asignatura_list.html"
    model = Asignatura
    http_method_names = [u'get', ]

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter()


class AsignaturaCreateView(CreateView):
    template_name = "asignatura_create.html"
    http_method_names = [u'get', u'post', ]
    success_url = '/asignaturas'
    form_class = AsignaturaModelForm


class AsignaturaUpdateView(UpdateView):
    template_name = "asignatura_create.html"
    http_method_names = [u'get', u'post', ]
    success_url = '/asignaturas'
    model = Asignatura
    form_class = AsignaturaModelForm


class AsignaturaDeleteView(DeleteView):
    template_name = "asignatura_delete.html"
    model = Asignatura
    success_url = '/asignaturas'
