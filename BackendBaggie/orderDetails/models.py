from django.db import models
from orders.models import Order
from products.models import Products
from users.models import CustomUser
# Create your models here.

class OrderDetails(models.Model):

    orderDetailsName= models.CharField(max_length=250, null=True)
    oder_ID         = models.ForeignKey(Order, on_delete=models.CASCADE)
    productID       = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    orderPrice      = models.DecimalField(max_digits=20, decimal_places=3, null=False)
    orderQuantity   = models.CharField(max_length=150, null=True)
    #owner           = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, null=True)


    """docstring forOrderDetails."""

    def __str__(self):
        return str(self.orderDetailsName)
