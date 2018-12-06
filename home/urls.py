from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='root_path'),
        url(r'^design/$', views.design, name="home.views.design"),
        url(r'^welcome/$', views.welcome, name="home.views.welcome"),
]
