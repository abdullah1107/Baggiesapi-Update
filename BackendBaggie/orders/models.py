from django.db import models
from users.models import CustomUser
from utils import create_new_ref_number
#from orderDetails.models import OrderDetails

# Create your models here.
class  Order(models.Model):
    customerID      = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, null=True)
    addressOne      = models.CharField(max_length=500, null=False)
    addressTwo      = models.CharField(max_length=450, null=True)
    city            = models.CharField(max_length=55, null=True, blank=True)
    phonenumber     = models.CharField(max_length=15, null=False)
    additionalnumber= models.CharField(max_length=15, null=True)
    orderemail      = models.EmailField(verbose_name = "email", max_length = 35, null=True)
    orderDate       = models.DateTimeField(auto_now=True)
    orderShipped    = models.BooleanField(default=False)
    #orderTrakingNumber= models.CharField(
           # max_length = 10,
           # blank=True,
           # editable=False,
           # unique=True,
           # default=create_new_ref_number())
    #
    # """docstring for  Order."""
    # class Meta:
    #     ordering: ['-orderDate']

    def __str__(self):
        return str(self.orderDate)

    # @property
    # def choices(self):
    #     return self.choice_set.all()
