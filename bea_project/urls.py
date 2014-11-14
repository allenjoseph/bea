from django.conf.urls import patterns, include, url
from django.contrib import admin
from bea.views import HomeView, UbicameView, LoginFormView
from pedidos.views import PedidosView
from precios.views import PreciosView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^ubicame/$', UbicameView.as_view(), name='ubicame'),
    url(r'^precios/$', PreciosView.as_view(), name='precios'),
    url(r'^pedidos/$', PedidosView.as_view(), name='pedidos'),
    url(r'^login/$', LoginFormView.as_view(), name='login'),
    url(r'^admin/', include(admin.site.urls)),
)
