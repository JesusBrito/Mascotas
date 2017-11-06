from django.conf.urls import url, include

from apps.usuario.views import RegistroUsuario

urlpatterns = [
    url(r'^registrar$', RegistroUsuario.as_view(),  name ='usuario_crear'),
]
