from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from django.template import RequestContext
from django.conf import settings
import shopify

def _return_address(request):
    return request.session.get('return_to') or reverse('root_path')

def login(request):
    # Ask user for their ${shop}.myshopify.com address

    # If the ${shop}.myshopify.com address is already provided in the URL,
    # just skip to authenticate
    if request.GET.get('shop'):
        return authenticate(request)
    return render(request, 'shopify_app/login.html', {})

def authenticate(request):
    shop = request.POST.get('shop')
    if shop:
        scope = settings.SHOPIFY_API_SCOPE
        redirect_uri = request.build_absolute_uri(reverse('shopify_app.views.finalize'))
        permission_url = shopify.Session(shop.strip()).create_permission_url(scope, redirect_uri)
        return redirect(permission_url)

    return redirect(_return_address(request))

def finalize(request):
    shop_url = request.GET.get('shop')
    try:
        shopify_session = shopify.Session(shop_url)
        request.session['shopify'] = {
            "shop_url": shop_url,
            "access_token": shopify_session.request_token(request.GET)
        }

    except Exception:
        messages.error(request, "Could not log in to Shopify store.")
        return redirect(reverse('shopify_app.views.login'))

    messages.info(request, "Logged in to shopify store.")

    response = redirect(_return_address(request))
    request.session.pop('return_to', None)
    return response

def logout(request):
    request.session.pop('shopify', None)
    messages.info(request, "Successfully logged out.")

    return redirect(reverse('shopify_app.views.login'))
