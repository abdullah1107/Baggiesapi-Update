from rest_framework import serializers
from productsImage.models import ProductImage

class ProductImageSerializer(serializers.ModelSerializer):
    ownerID = serializers.ReadOnlyField(source='owner.id')
    class Meta:
        model = ProductImage
        fields = ('id','productID','image', 'updated_at','ownerID')
