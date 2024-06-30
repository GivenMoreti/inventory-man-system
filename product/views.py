from .models import Product
from django.shortcuts import render, redirect
from .forms import ProductForm
from django.core.paginator import Paginator


def get_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 5)  # Show 10 products per page
    page_number = request.GET.get('page')
    product_count = Product.objects.count()
    page_obj = paginator.get_page(page_number)
    return render(request, 'product/products.html', {'page_obj': page_obj,"product_count":product_count})



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_products')  # Redirect to a product list page or another view
    else:
        form = ProductForm()
    return render(request, 'product/add_product.html', {'form': form})
