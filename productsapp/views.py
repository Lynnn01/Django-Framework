from django.shortcuts import render
from productsapp.models import *
# Create your views here.


def index(request):
    products = Product.objects.filter(isTrending=True)
    print(products)
    return render(request, 'index.html', {"products": products},)


def productDetail(request, id):
    product_detail = Product.objects.get(id=id)
    return render(request, 'detail.html', {"details": product_detail},)


def products(request, ):
    products = Product.objects.all()
    return render(request, 'product.html',{"products": products})
