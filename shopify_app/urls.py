from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
        url(r'^$', 'shopify_app.views.login'),
        url(r'^authenticate/$', 'shopify_app.views.authenticate'),
        url(r'^finalize/$', 'shopify_app.views.finalize'),
        url(r'^logout/$', 'shopify_app.views.logout'),
)
