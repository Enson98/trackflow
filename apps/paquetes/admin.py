from django.contrib import admin
from .models import Paqueteria, Estatus, Paquete, HistorialCambio

@admin.register(Paqueteria)
class PaqueteriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'activa', 'created_at']
    list_filter = ['activa']

@admin.register(Estatus)
class EstatusAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'color', 'orden']
    list_editable = ['orden']

@admin.register(Paquete)
class PaqueteAdmin(admin.ModelAdmin):
    list_display = ['numero_guia', 'cliente', 'paqueteria', 'estatus', 'fecha_envio']
    list_filter = ['estatus', 'paqueteria', 'fecha_envio']
    search_fields = ['numero_guia', 'cliente__nombre']
    date_hierarchy = 'fecha_envio'

@admin.register(HistorialCambio)
class HistorialCambioAdmin(admin.ModelAdmin):
    list_display = ['paquete', 'campo_modificado', 'usuario', 'created_at']
    list_filter = ['campo_modificado', 'created_at']