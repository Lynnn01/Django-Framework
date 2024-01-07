from django.shortcuts import render
from productsapp.models import *
# Create your views here.


def index(request):
    products = Product.objects.filter(isTrending=True)
    print(products)
    return render(request,
                  'index.html',
                  {"products": products},
                  )
