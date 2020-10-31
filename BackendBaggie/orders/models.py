from django.db import models
from customers.models import Customer

# Create your models here.
class  Order(models.Model):
    owner           = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    orderAmount     = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    addressOne      = models.CharField(max_length=500, null=False)
    addressTwo      = models.CharField(max_length=450, null=True)
    city            = models.CharField(max_length=350, null=False)
    country         = models.CharField(max_length=350, null=True)
    orderPhoneNumber= models.CharField(max_length=15, null=False)
    otherPhoneNunber= models.CharField(max_length=15, null=True)
    orderemail      = models.EmailField(verbose_name = "email", max_length = 35, null=True)
    orderDate       = models.DateTimeField(auto_now=True)
    orderShipped    = models.BooleanField(default=False)
    orderTrakingNumber= models.CharField(max_length=550, null=True)

    """docstring for  Order."""
    class Meta:
        ordering: ['-orderDate']

    def __str__(self):
        return str(self.orderShipped)
