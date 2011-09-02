from django.shortcuts import render_to_response
from django.template import RequestContext
import shopify
from shopify_app.decorators import shop_login_required

def welcome(request):
    return render_to_response('home/welcome.html', {
        'callback_url': "http://%s/login/finalize" % (request.get_host()),
    }, context_instance=RequestContext(request))

@shop_login_required
def index(request):
    products = shopify.Product.find(limit=3)
    orders = shopify.Order.find(limit=3, order="created_at DESC")
    return render_to_response('home/index.html', {
        'products': products,
        'orders': orders,
    }, context_instance=RequestContext(request))

def design(request):
    return render_to_response('home/design.html', {},
                              context_instance=RequestContext(request))
