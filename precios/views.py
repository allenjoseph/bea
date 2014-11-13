from django.views.generic import TemplateView	
from bea.mixins import JsonResponseMixin

class PreciosView(JsonResponseMixin, TemplateView):
	template_name = 'precios.html'
