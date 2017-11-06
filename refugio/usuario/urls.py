from django.conf.urls import url, include

from apps.usuario.views import RegistroUsuario

urlpatterns = [
    url(r'^registrar$', RegistrarUsuario.as_view(),  name ='usuario_crear'),
]
