from rest_framework import serializers
from productsCategory.models import ProductsCategory
from users.models import CustomUser
#from users.serializers import CustomUserSerilizer


class ProductsCategorySerializer(serializers.ModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.id')
	class Meta:
		model = ProductsCategory
		fields = ('id','categoryName','created_at', 'updated_at','owner')
