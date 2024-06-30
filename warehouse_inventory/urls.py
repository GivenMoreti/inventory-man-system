from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.get_warehouse_inventories,name="get_warehouse_inventories"),
    
]