from django.db import models
from django.contrib.auth.models import User
from apps.core.models import BaseModel

class Incidencia(BaseModel):
    """Incidencias en paquetes"""
    paquete = models.ForeignKey(
        'paquetes.Paquete',
        on_delete=models.CASCADE,
        related_name='incidencias'
    )
    
    tipo = models.CharField(max_length=100)  # "Retraso", "Extravío", etc.
    descripcion = models.TextField()
    
    resuelta = models.BooleanField(default=False)
    solucion = models.TextField(blank=True)
    
    reportado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='incidencias_reportadas'
    )
    
    fecha_resolucion = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        db_table = 'incidencias'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.paquete.numero_guia} - {self.tipo}"