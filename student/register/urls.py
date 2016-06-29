from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.Index, name='index'),
    url(r'^create/$', views.Create, name='create'),
    url(r'^login/$', views.login, name='login'),
    url(r'^Authorized/$', views.Authorized, name='Authorized'),
]
