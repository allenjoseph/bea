from django.views.generic import TemplateView	
from bea.mixins import JsonResponseMixin

class PedidosView(JsonResponseMixin, TemplateView):
	template_name = 'pedidos.html'
