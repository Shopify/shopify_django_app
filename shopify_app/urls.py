from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.login, name="shopify_app.views.login"),
        url(r'^authenticate/$', views.authenticate, name="shopify_app.views.authenticate"),
        url(r'^finalize/$', views.finalize, name="shopify_app.views.finalize"),
        url(r'^logout/$', views.logout, name="shopify_app.views.logout"),
]
