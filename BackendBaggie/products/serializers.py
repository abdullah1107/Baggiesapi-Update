from rest_framework import serializers
from products.models import Products
from productsCategory.serializers import  ProductsCategorySerializer
from productsCategory.models import ProductsCategory
from productsImage.serializers import ProductImageSerializer
# from products.models import ProductImage

# class ProductImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductImage
#         fields = ('image',)


class ProductsSerializer(serializers.ModelSerializer):

    product_image  = ProductImageSerializer(many=True,read_only = True)
    class Meta:
        model = Products
        fields = ('id',
        'productname',
        'productpriceoriginal',
        'productpricesell',
        'percentageofsell',
        'productweight',
        'productinstock',
        'productcoverImage',
        'productDetails',
        'productUpdate',
        'productdiscount',
        'productapprovalstatus',
        'isrecentproduct',
        'product_image',
        'vendorID',
        'productcategoryID')




        
    # def create(self, validated_data):
    #     images_data = self.context.get('images').request.FILES
    #     product = Products.objects.create(productName=validated_data.get('productName'),
    #        productcategoryID_id=1)
    #     for image_data in images_data:
    #         ProductImage.objects.create(product=product, **image_data)
    #     return product
    # def create(self, validated_data):
    #     images_data = self.context.get('view').request.FILES
    #     product = Products.objects.create(productName=validated_data.get('productName'),
    #                                productID_id=1)
    #     for image_data in images_data.values():
    #         ProductImage.objects.create(product=product, productImage=image_data)
    #     return product
