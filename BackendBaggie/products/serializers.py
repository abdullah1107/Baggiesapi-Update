from rest_framework import serializers
from products.models import Products
from productsImage.models import ProductImage
from productsCategory.serializers import  ProductsCategorySerializer
from productsCategory.models import ProductsCategory
from productsImage.serializers import ProductNestedImageSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
# from products.models import ProductImage

# class ProductImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductImage
#         fields = ('image',)


class ProductsSerializer(WritableNestedModelSerializer):
    product_image  = ProductNestedImageSerializer(many=True)
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
        'vendorID',
        'productcategoryID',
        'product_image')

    # def create(self, validated_data):
    #     images_data = self.context.get('view').request.FILES
    #     product = Products.objects.create(productname=validated_data.get('productname', 'no-productname'))
    #     for image_data in images_data.values():
    #         ProductImage.objects.create(image=image_data)
    #     return product


    # def create(self, validated_data):
    #     images_data = self.context.get('product_image').request.FILES
    #     product = Products.objects.create(**validated_data)
    #     for image_data in images_data:
    #         ProductImage.objects.create(**image_data, product=product)
    #     return product
    # def create(self, validated_data):
    #     images_data = self.context.get('view').request.FILES
    #     product = Products.objects.create(productName=validated_data.get('productName'),
    #                                productID_id=1)
    #     for image_data in images_data.values():
    #         ProductImage.objects.create(product=product, productImage=image_data)
    #     return product
