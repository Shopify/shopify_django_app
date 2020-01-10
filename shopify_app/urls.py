from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='shopify_app_login'),
    path('authenticate/', views.authenticate, name='shopify_app_authenticate'),
    path('finalize/', views.finalize, name='shopify_app_login_finalize'),
    path('logout/', views.logout, name='shopify_app_logout'),
]
