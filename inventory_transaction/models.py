from django.db import models
from product.models import Product

# Create your models here.
class InventoryTransaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20, choices=[('IN', 'In'), ('OUT', 'Out')])
    quantity = models.IntegerField()
    transaction_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True,null=True)
    date_edited = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f"{self.transaction_type} {self.quantity} of {self.product.name}"
