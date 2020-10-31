from rest_framework import serializers
from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    #ownerID = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = Order
        fields = ('id',
        'owner',
        'addressOne',
        'addressTwo',
        'city',
        'country',
        'orderPhoneNumber',
        'otherPhoneNunber',
        'orderemail',
        'orderDate',
        'orderShipped',
        'orderTrakingNumber'
        )
