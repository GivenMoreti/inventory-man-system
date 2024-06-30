from django.shortcuts import render
from .models import Warehouse

# Create your views here.
def get_warehouses(request):
    warehouses = Warehouse.objects.all()
    warehouse_count = Warehouse.objects.count()
    context = {"warehouses":warehouses,"warehouse_count":warehouse_count}
    return render(request,"warehouse/warehouses.html",context)