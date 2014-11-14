from django.views.generic import TemplateView	
from bea.mixins import JsonResponseMixin, LoginRequiredMixin


class PedidosView(LoginRequiredMixin, JsonResponseMixin, TemplateView):
    template_name = 'pedidos.html'

    
