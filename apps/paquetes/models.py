from django.db import models
from django.contrib.auth.models import User
from apps.core.models import BaseModel

class Paqueteria(BaseModel):
    """Empresas de paquetería"""
    nombre = models.CharField(max_length=100, unique=True)
    activa = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'paqueterias'
        verbose_name = 'Paquetería'
        verbose_name_plural = 'Paqueterías'
    
    def __str__(self):
        return self.nombre


class Estatus(BaseModel):
    """Catálogo de estatus personalizados"""
    nombre = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7, default='#3B82F6')  # Color hex
    orden = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'estatus'
        ordering = ['orden']
        verbose_name = 'Estatus'
        verbose_name_plural = 'Estatus'
    
    def __str__(self):
        return self.nombre


class Paquete(BaseModel):
    """Paquete/Envío principal"""
    # Identificadores
    numero_guia = models.CharField(max_length=100, unique=True, db_index=True)
    
    # Relaciones
    cliente = models.ForeignKey(
        'accounts.Cliente',
        on_delete=models.PROTECT,
        related_name='paquetes'
    )
    paqueteria = models.ForeignKey(
        Paqueteria,
        on_delete=models.PROTECT,
        related_name='paquetes'
    )
    estatus = models.ForeignKey(
        Estatus,
        on_delete=models.PROTECT,
        related_name='paquetes'
    )
    
    # Ubicaciones
    origen = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    
    # Fechas
    fecha_registro = models.DateField()
    fecha_envio = models.DateField(null=True, blank=True)
    fecha_entrega = models.DateField(null=True, blank=True)
    
    # Información adicional
    observaciones = models.TextField(blank=True)
    
    # Auditoría
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='paquetes_creados'
    )
    
    class Meta:
        db_table = 'paquetes'
        ordering = ['-fecha_registro', '-created_at']
        indexes = [
            models.Index(fields=['numero_guia']),
            models.Index(fields=['estatus', 'fecha_registro']),
        ]
    
    def __str__(self):
        return f"{self.numero_guia} - {self.cliente.nombre}"


class HistorialCambio(BaseModel):
    """Trazabilidad de cambios en paquetes"""
    paquete = models.ForeignKey(
        Paquete,
        on_delete=models.CASCADE,
        related_name='historial'
    )
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    campo_modificado = models.CharField(max_length=50)
    valor_anterior = models.TextField(blank=True)
    valor_nuevo = models.TextField()
    
    class Meta:
        db_table = 'historial_cambios'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.paquete.numero_guia} - {self.campo_modificado}"