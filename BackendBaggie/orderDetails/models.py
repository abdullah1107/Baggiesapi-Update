from django.db import models
from orders.models import Order
from products.models import Products
from users.models import CustomUser
# Create your models here.

class OrderDetails(models.Model):

    orderDetailsName= models.CharField(max_length=250, null=True, blank=True)
    oderID          = models.ForeignKey(Order, on_delete=models.CASCADE)
    productID       = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    orderprice      = models.DecimalField(max_digits=150, decimal_places=3, null=False)
    orderQuantity   = models.CharField(max_length=150, null=True)
    toalprice       = models.DecimalField(max_digits=150, decimal_places=3, null=False)

    """docstring forOrderDetails."""

    def __str__(self):
        return str(self.orderDetailsName)
