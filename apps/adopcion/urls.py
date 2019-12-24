from django.urls import path
from . import views
from apps.adopcion.views import index, SolicitudList,SolicitudCreate,SolicitudUpdate,SolicitudDelete

app_name='adopcion'

urlpatterns = [
    path('', views.index, name='index'),
    path('solictud/listar', SolicitudList.as_view(), name='solicitud_listar'),
    path('solictud/nueva', SolicitudCreate.as_view(), name='solicitud_crear'),
    path('solictud/editar/<int:pk>', SolicitudUpdate.as_view(), name='solicitud_editar'),
    path('solicitud/eliminar/<int:pk>',SolicitudDelete.as_view(),name='solicitud_eliminar'),
]