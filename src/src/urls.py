from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from apps.home.views import (HomeView, Ejercicios)

# from apps.parcial.views import Parte1View, Parte2View


urlpatterns = [
    url(r'^$', HomeView.as_view()),
    url(r'^(?P<t>[\w]+)/(?P<n>[0-9]+)$', Ejercicios.as_view()),

    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
