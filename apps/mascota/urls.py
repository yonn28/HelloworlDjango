from django.urls import path
from apps.mascota.views import index, mascota_view

urlpatterns = [
    path('', index, name='mascota'),
    path('nuevo', mascota_view, name='mascota_crear'),
]
