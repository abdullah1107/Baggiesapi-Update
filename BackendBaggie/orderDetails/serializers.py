from rest_framework import serializers
from orderDetails.models import OrderDetails
#from users.models import CustomUser
from orders.models import Order
from products.models import Products

class OrderDetailsSerializer(serializers.ModelSerializer):
    #owner_ID = serializers.ReadOnlyField(source='owner.id')
    order_ID = serializers.ReadOnlyField(source='order_ID.id')
    class Meta:
        model = OrderDetails
        fields = ('id','productID','order_ID','orderDetailsName','orderPrice','orderQuantity')
