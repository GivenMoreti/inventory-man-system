from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.get_orders,name="get_orders")
]