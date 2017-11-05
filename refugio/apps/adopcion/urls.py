from django.conf.urls import url, include
from apps.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate,SolicitudUpdate,SolicitudDelete

urlpatterns = [
	url(r'^index$',index_adopcion),
	url(r'^listar$',SolicitudList.as_view(), name='solicitud_listar'),
	url(r'^nueva$',SolicitudCreate.as_view(), name='solicitud_crear'),
	url(r'^editar/(?P<pk>\d+)/$',SolicitudUpdate.as_view(), name='solicitud_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$',SolicitudDelete.as_view(), name='solicitud_eliminar'),
]