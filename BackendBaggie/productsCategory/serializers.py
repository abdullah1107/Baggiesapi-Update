from rest_framework import serializers
from productsCategory.models import ProductsCategory


class ProductsCategorySerializer(serializers.ModelSerializer):
	#owner = serializers.ReadOnlyField(source='owner.id')
	class Meta:
		model = ProductsCategory
		fields = ('id','categoryName','created_at', 'updated_at','vendorID')

class ProductCategoryCreateSerializer(serializers.ModelSerializer):
	#categoryName = serializers.CharField(max_length=15, write_only=True)
	class Meta:
		model = ProductsCategory
		fields = ('id','categoryName','created_at', 'updated_at','vendorID')

		def save(self):
			try:
				categoryName = self.validated_data['categoryName']
				created_at   = self.validated_data['created_at']
				updated_at   = self.validated_data['updated_at']
				ownerID        = self.validated_data['vendorID']

				pcategory    = ProductsCategory(
				             categoryName=categoryName,
							 created_at  = created_at,
							 updated_at  = updated_at,
							 vendorID       = vendorID)
				pcategory.save()
				return pcategory
			except KeyError:
				raise serializers.ValidationError({"reason":"something error"})
