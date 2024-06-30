from django.shortcuts import render
from .models import Product


def get_products(request):
    products = Product.objects.all()
    context = {"products":products}
    return render(request,"product/products.html",context)