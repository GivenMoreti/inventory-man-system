from django.shortcuts import render
from .models import OrderItem

# Create your views here.
def get_order_items(request):
    orderItems = OrderItem.objects.all()
    context = {"orderItems":orderItems}
    return render(request,"orderitem/orderitem.html",context)