from django.db import models
from warehouse.models import Warehouse
from product.models import Product

# Create your models here.
class WarehouseInventory(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} in {self.warehouse.name}: {self.quantity}"
