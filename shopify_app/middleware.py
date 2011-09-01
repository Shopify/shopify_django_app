from django.conf import settings
from django.core.urlresolvers import reverse
import shopify

class ConfigurationError(StandardError):
    pass

class LoginProtection(object):
    def __init__(self):
        if not settings.SHOPIFY_API_KEY or not settings.SHOPIFY_API_SECRET:
            raise ConfigurationError("SHOPIFY_API_KEY and SHOPIFY_API_SECRET must be set in settings")
        shopify.Session.setup(api_key=settings.SHOPIFY_API_KEY,
                              secret=settings.SHOPIFY_API_SECRET)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if hasattr(request, 'session') and 'shopify' in request.session:
            shopify.ShopifyResource.site = request.session['shopify'].site

    def process_response(self, request, response):
        shopify.ShopifyResource.site = None
        return response
