# -*- encoding: utf-8 -*-

from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, FormView
from bea.forms import LoginForm
from bea.mixins import JsonResponseMixin

class PreviousView(JsonResponseMixin, TemplateView):
    template_name = 'previous.html'

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
        usuario = form.cleaned_data['usuario']
        password = form.cleaned_data['password']

        user = authenticate(username=usuario, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
            else:                
                form.add_error(None, "El usuario ha sido deshabilitado.")
                return super(LoginFormView, self).form_invalid(form)
        else:
            form.add_error(None, "El usuario o contraseña son incorrectos.")
            return super(LoginFormView, self).form_invalid(form)

        return super(LoginFormView, self).form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next', False)
        if next_url:
            self.success_url = next_url
        return super(LoginFormView, self).get_success_url()

            
class UbicameView(JsonResponseMixin, TemplateView):
    pass
