from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^forms$', views.forms, name='forms'),
    url(r'^get_name$', views.get_name, name='get_name'),
    
]
