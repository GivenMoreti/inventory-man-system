from django.db import models
from supplier.models import Supplier
from product.models import Product

# Create your models here.
class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    order_date = models.DateField(auto_now_add=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.order_number
