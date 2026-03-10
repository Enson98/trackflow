from django.urls import path
from . import views

app_name = 'paquetes'

urlpatterns = [
    path('', views.ListadoPaquetesView.as_view(), name='listado'),
]