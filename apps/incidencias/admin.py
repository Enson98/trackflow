from django.contrib import admin
from .models import Incidencia

@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ['paquete', 'tipo', 'resuelta', 'reportado_por', 'created_at']
    list_filter = ['resuelta', 'tipo']