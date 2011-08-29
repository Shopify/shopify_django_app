from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^login/', include('shopify_app.urls')),
    url(r'^', include('home.urls'), name='root_path'),
)
