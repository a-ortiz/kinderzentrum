from django.conf.urls import patterns, url
from pago import views

urlpatterns = [
  url(r'^$',  pago.index_view, name='index_view')
]
