from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^$', 'home.views.index', name='root_path'),
        url(r'^design/$', 'home.views.design'),
        url(r'^welcome/$', 'home.views.welcome'),
)
