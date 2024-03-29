from rest_framework import serializers
from cartview.models import CartVeiw

class CartVeiwCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartVeiw
        fields = ('id','productID', 'customerID', 'review_at')

class CartVeiwSerializer(serializers.ModelSerializer):
    customerid   = serializers.CharField(source='customerID.id', read_only=True)
    customername = serializers.CharField(source='customerID.name', read_only=True)
    phonenumber = serializers.CharField(source='customerID.mobileNumber', read_only=True)
    email = serializers.CharField(source='customerID.email', read_only=True)

    class Meta:
        model = CartVeiw
        fields = ('id','productID', 'review_at','customerid','customername','phonenumber','email')
        depth = 1
