from rest_framework import serializers
from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
        'id',
        'customerID',
        'addressOne',
        'addressTwo',
        'city',
        'phonenumber',
        'additionalnumber',
        'orderemail',
        'orderDate',
        'orderShipped',
        'orderTrakingNumber'
        )
