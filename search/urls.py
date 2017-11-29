from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.login, name='main'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^forms$', views.forms, name='forms'),
    url(r'^search$', views.search, name='search'),
    url(r'^get_at$', views.get_at, name='get_at'),
    url(r'^get_name$', views.get_name, name='get_name'),
    url(r'^message$', views.message, name='message'),
    url(r'^intersection$', views.intersection, name='intersection'),
]
