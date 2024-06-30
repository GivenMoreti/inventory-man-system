from django.shortcuts import render
from .models import Warehouse

# Create your views here.
def get_warehouses(request):
    warehouses = Warehouse.objects.all()
    context = {"warehouses":warehouses}
    return render(request,"warehouse/warehouses.html",context)