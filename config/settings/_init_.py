# Este archivo permite importar settings como módulo
from decouple import config

# Determina qué settings usar
settings_module = config('DJANGO_SETTINGS_MODULE', default='config.settings.development')

if 'production' in settings_module:
    from .production import *
else:
    from .development import *