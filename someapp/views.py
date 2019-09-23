from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Product


def index(request):

    context = {
        "products": Product.objects.all()
    }
    return render(request, "products/index.html", context)


def product_info(request, product_id):
    
    print(product_id)

    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    
    context = {
        "product" : product
    }
    return render(request, "products/product_page.html", context)