from django.shortcuts import render
from .models import Supplier
# Create your views here.

def get_suppliers(request):
    suppliers = Supplier.objects.all()
    supplier_count = Supplier.objects.count()
    context = {"suppliers":suppliers,"supplier_count":supplier_count}
    return render(request,"supplier/suppliers.html",context)