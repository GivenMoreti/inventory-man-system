from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.get_categories,name="get_categories"),
    
]