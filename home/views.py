from django.shortcuts import render
from django.template import RequestContext
import shopify
from shopify_app.decorators import shop_login_required

def welcome(request):
    return render(request, 'home/welcome.html', {
        'callback_url': "http://%s/login/finalize" % (request.get_host()),
    })

@shop_login_required
def index(request):
    products = shopify.Product.find(limit=3)
    orders = shopify.Order.find(limit=3, order="created_at DESC")
    return render(request, 'home/index.html', {
        'products': products,
        'orders': orders,
    })

def design(request):
    return render(request, 'home/design.html', {})
