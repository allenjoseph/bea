from django.views.generic import TemplateView
from bea.mixins import JsonResponseMixin


class HomeView(JsonResponseMixin, TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return self.response_handler()

    def get_data(self):
        is_auth = False
        if self.request.user.is_authenticated():
            is_auth = True
        data = {
            'is_auth': is_auth,
            'app': 'Bea App'
        }
        return data


class UbicameView(JsonResponseMixin, TemplateView):
    pass
