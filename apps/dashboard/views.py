from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from apps.paquetes.models import Paquete

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # KPIs básicos
        context['total_paquetes'] = Paquete.objects.count()
        context['con_incidencias'] = Paquete.objects.filter(
            incidencias__resuelta=False
        ).distinct().count()
        
        # Paquetes por estatus
        context['paquetes_por_estatus'] = Paquete.objects.values(
            'estatus__nombre', 'estatus__color'
        ).annotate(total=Count('id'))
        
        return context