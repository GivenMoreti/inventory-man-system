from django.shortcuts import render
from .models import Category

# Create your views here.
def get_categories(request):
    categories = Category.objects.all()
    context = {"categories":categories}
    
    return render(request,"category/categories.html",context)