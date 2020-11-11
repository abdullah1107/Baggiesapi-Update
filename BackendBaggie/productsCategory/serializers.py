from rest_framework import serializers
from productsCategory.models import ProductsCategory


class ProductsCategorySerializer(serializers.ModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.id')
	class Meta:
		model = ProductsCategory
		fields = ('id','categoryName','created_at', 'updated_at','owner')

# class ProductCategoryCreateSerializer(serializers.ModelSerializer):
# 	#categoryName = serializers.CharField(max_length=15, write_only=True)
# 	class Meta:
# 		model = ProductsCategory
# 		fields = ('id','categoryName','created_at', 'updated_at','owner')
#
# 		def save(self):
# 			try:
# 				categoryName = self.validated_data['categoryName']
# 				created_at   = self.validated_data['created_at']
# 				updated_at   = self.validated_data['updated_at']
# 				owner        = self.validated_data['owner']
#
# 				pcategory    = ProductsCategory(
# 				             categoryName=categoryName,
# 							 created_at  = created_at,
# 							 updated_at  = updated_at,
# 							 owner       = owner)
# 				pcategory.save()
# 				return pcategory
# 			except KeyError:
# 				raise serializers.ValidationError({"reason":"something error"})
