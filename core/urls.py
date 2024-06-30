
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("products/",include("product.urls")),
    path("categories/",include("category.urls")),
    path("warehouses/",include("warehouse.urls")),
    path("orders/",include("order.urls")),
    path("orderitems/",include("orderitem.urls")),
    path("suppliers/",include("supplier.urls")),
    path("inventory_transaction/",include("inventory_transaction.urls")),

]
