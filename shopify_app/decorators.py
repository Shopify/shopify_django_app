from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from . import views

def shop_login_required(fn):
    def wrapper(request, *args, **kwargs):
        if not hasattr(request, 'session') or 'shopify' not in request.session:
            request.session['return_to'] = request.get_full_path()
            return redirect(reverse(views.login))
        return fn(request, *args, **kwargs)
    wrapper.__name__ = fn.__name__
    return wrapper
