from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Paquete

class ListadoPaquetesView(LoginRequiredMixin, ListView):
    model = Paquete
    template_name = 'paquetes/listado.html'
    context_object_name = 'paquetes'
    paginate_by = 50