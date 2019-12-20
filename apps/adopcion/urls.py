from django.urls import path
from . import views

appname='adopcion'

urlpatterns = [
    path('', views.index, name='adopcion'),
]