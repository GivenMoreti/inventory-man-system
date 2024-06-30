from django.shortcuts import render
from .models import Category

# Create your views here.
def get_categories(request):
    categories = Category.objects.all()
    
    cat_count = Category.objects.count()
    context = {"categories":categories,"cat_count":cat_count}
    return render(request,"category/categories.html",context)