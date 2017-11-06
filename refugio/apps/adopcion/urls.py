from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate,SolicitudUpdate,SolicitudDelete

urlpatterns = [
	url(r'^index$',index_adopcion),
	url(r'^listar$',login_required(SolicitudList.as_view()), name='solicitud_listar'),
	url(r'^nueva$',login_required(SolicitudCreate.as_view()), name='solicitud_crear'),
	url(r'^editar/(?P<pk>\d+)/$',login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$',login_required(SolicitudDelete.as_view()), name='solicitud_eliminar'),
]