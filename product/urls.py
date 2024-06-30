from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.get_products,name="get_products"),
    path("add_product/",views.add_product,name="add_product"),
    
]