from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.get_orders,name="get_orders"),
    path("create_order/",views.create_order,name="create_order"),
    path('generate_receipt/<int:order_id>/', views.generate_receipt, name='generate_receipt'),
]