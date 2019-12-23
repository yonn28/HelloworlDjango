from django.urls import path
from apps.mascota.views import index, mascota_view,mascota_list,mascota_edit,mascota_delete, MascotaList,MascotaCreate,MascotaUpdate,MascotaDelete

app_name='mascota'

urlpatterns = [
    path('', index, name='index'),
    # path('nuevo', mascota_view, name='mascota_crear'),
    path('nuevo', MascotaCreate.as_view(), name='mascota_crear'),
    # path('listar', mascota_list, name='mascota_listar'),
    path('listar',MascotaList.as_view(),name='mascota_listar'),
    #path('editar/<int:pk>/', mascota_edit, name='mascota_editar'),
    path('editar/<int:pk>/', MascotaUpdate.as_view(), name='mascota_editar'),
    # path('eliminar/<int:id_mascota>',mascota_delete,name='mascota_borrar'),
    path('eliminar/<int:pk>/', MascotaDelete.as_view(), name='mascota_borrar'),
]
