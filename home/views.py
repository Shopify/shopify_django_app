from django.shortcuts import render
import shopify
from shopify_app.decorators import shop_login_required

@shop_login_required
def index(request):
    products = shopify.Product.find(limit=3)
    orders = shopify.Order.find(limit=3, order="created_at DESC")
    page_data = {
        'products': products,
        'orders': orders,
    }
    return render(request, 'home/index.html', page_data)
