from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from apps.home.views import (HomeView, Ejercicios,
                             EstudianteListView, EstudianteCreateView, EstudianteUpdateView, EstudianteDeleteView,
                             AsignaturaListView, AsignaturaCreateView, AsignaturaUpdateView, AsignaturaDeleteView)

# from apps.parcial.views import Parte1View, Parte2View


urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^estudiantes$', EstudianteListView.as_view(), name="estudiantes_list"),
    url(r'^estudiantes/crear$', EstudianteCreateView.as_view(), name="estudiantes_create"),
    url(r'^estudiantes/actualizar/(?P<slug>[\w]+)$', EstudianteUpdateView.as_view(), name="estudiantes_update"),
    url(r'^estudiantes/eliminar/(?P<slug>[\w]+)$', EstudianteDeleteView.as_view(), name="estudiantes_delete"),

    url(r'^asignaturas$', AsignaturaListView.as_view(), name="asignaturas_list"),
    url(r'^asignaturas/crear$', AsignaturaCreateView.as_view(), name="asignaturas_create"),
    url(r'^asignaturas/actualizar/(?P<pk>[\w]+)$', AsignaturaUpdateView.as_view(), name="asignaturas_update"),
    url(r'^asignaturas/eliminar/(?P<pk>[\w]+)$', AsignaturaDeleteView.as_view(), name="asignaturas_delete"),

    url(r'^(?P<t>[\w]+)/(?P<n>[0-9]+)$', Ejercicios.as_view()),

    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
