# TrackFlow MVP - Sistema de Seguimiento de Paquetería

Sistema web para gestión y seguimiento de envíos de paquetería.

## Stack Tecnológico

- **Backend:** Django 5.0
- **Frontend:** HTMX + Tailwind CSS
- **Base de datos:** PostgreSQL 16
- **Deployment:** Railway.app

## Desarrollo Local

### Con Docker (Recomendado)
```bash
# Clonar repositorio
git clone <repo-url>
cd trackflow

# Levantar servicios
docker-compose up

# En otra terminal: migraciones
docker-compose exec web python manage.py migrate

# Crear superusuario
docker-compose exec web python manage.py createsuperuser
```

Accede a: http://localhost:8000

### Sin Docker
```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar .env
cp .env.example .env

# Migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Correr servidor
python manage.py runserver
```

## Estructura del Proyecto
```
trackflow/
├── apps/                 # Aplicaciones Django
│   ├── accounts/        # Autenticación y clientes
│   ├── paquetes/        # Gestión de paquetes
│   ├── incidencias/     # Reportes de problemas
│   ├── importar/        # Carga masiva Excel
│   └── dashboard/       # Vista principal
├── config/              # Configuración Django
├── templates/           # Templates HTML
└── static/              # Archivos estáticos
```

## Comandos Útiles
```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Acceder a shell
python manage.py shell

# Crear superusuario
python manage.py createsuperuser
```