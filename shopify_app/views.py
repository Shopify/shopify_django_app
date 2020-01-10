from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.template import RequestContext
from django.apps import apps
import shopify

def _return_address(request):
    return request.session.get('return_to') or reverse('root_path')

def _shop(request):
    shop_url = request.GET.get('shop', request.POST.get('shop'))
    if not shop_url:
        messages.error(request, "A shop param is required")
        return redirect(reverse(login))
    return shop_url.strip()

def _new_session(shop_url):
    api_version = apps.get_app_config('shopify_app').SHOPIFY_API_VERSION
    return shopify.Session(shop_url, api_version)

# Ask user for their ${shop}.myshopify.com address
def login(request):
    # If the ${shop}.myshopify.com address is already provided in the URL,
    # just skip to authenticate
    if request.GET.get('shop'):
        return authenticate(request)
    return render(request, 'shopify_app/login.html', {})

def authenticate(request):
    shop_url = _shop(request)
    scope = apps.get_app_config('shopify_app').SHOPIFY_API_SCOPE
    redirect_uri = request.build_absolute_uri(reverse(finalize))
    permission_url = _new_session(shop_url).create_permission_url(scope, redirect_uri)
    return redirect(permission_url)

def finalize(request):
    #try:
    shop_url = _shop(request)
    session = _new_session(shop_url)
    request.session['shopify'] = {
        "shop_url": shop_url,
        "access_token": session.request_token(request.GET)
    }
    # except Exception:
    #     messages.error(request, "Could not log in to Shopify store.")
    #     return redirect(reverse(login))
    messages.info(request, "Logged in to shopify store.")
    request.session.pop('return_to', None)
    return redirect(_return_address(request))

def logout(request):
    request.session.pop('shopify', None)
    messages.info(request, "Successfully logged out.")
    return redirect(reverse(login))
