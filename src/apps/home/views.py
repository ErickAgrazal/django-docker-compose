# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Estudiante


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
        return qs.filter(edad=35)
