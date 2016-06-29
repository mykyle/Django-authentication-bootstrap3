from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search-form/$', views.search_form),
    url(r'^search-form/search/$', views.search),
     url(r'^contact/$', views.contact),
]
