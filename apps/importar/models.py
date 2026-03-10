from django.db import models
from django.contrib.auth.models import User
from apps.core.models import BaseModel

class ImportacionExcel(BaseModel):
    """Registro de importaciones masivas"""
    archivo = models.FileField(upload_to='importaciones/%Y/%m/')
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    total_filas = models.IntegerField(default=0)
    filas_exitosas = models.IntegerField(default=0)
    filas_error = models.IntegerField(default=0)
    
    errores = models.TextField(blank=True)
    
    class Meta:
        db_table = 'importaciones_excel'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Importación {self.id} - {self.created_at.strftime('%d/%m/%Y')}"
