from django.shortcuts import render
from .models import Order
# Create your views here.
def get_orders(request):
    orders = Order.objects.all()
    order_count = Order.objects.count()
    context = {"orders":orders,"order_count":order_count}
    return render(request,"order/orders.html",context)