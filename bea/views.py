from django.views.generic import TemplateView, FormView
from bea.forms import LoginForm
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

class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

class UbicameView(JsonResponseMixin, TemplateView):
    pass
