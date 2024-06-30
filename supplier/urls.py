from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.get_suppliers,name="get_suppliers"),
  

]