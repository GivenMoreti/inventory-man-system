from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.get_order_items,name="get_order_items")
]