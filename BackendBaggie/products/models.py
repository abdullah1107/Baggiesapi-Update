from django.db import models
from users.models import CustomUser
from productsCategory.models import ProductsCategory
# Create your models here.
def upload_productCoverImage(instance, filename, **kwargs):
	file_path = 'prodcutCoverImage/{productID}/{productName}-{filename}'.format(
			productID = str(instance.productID),imageName=str(instance.productName), filename=filename
		)
	return file_path

class Products(models.Model):
    CATEGORY_OPTIONS = [
          ('is_new', 'is_new'),
          ('not_new', 'not_new')
      ]
    productName     = models.CharField(max_length=350, null=True)
    productPrice    = models.DecimalField(max_digits=20, decimal_places=3, null=True)
    productWeight   = models.CharField(max_length = 35, null = True)
    productInStock  = models.CharField(max_length = 30, null=True)
    productCoverImage= models.ImageField(upload_to='upload_productCoverImage',null=True)
    productDetails  = models.TextField(null=True)
    productImage    = models.FileField(blank=True)
    productUpdate   = models.DateTimeField(auto_now=True)
    productdiscount = models.BooleanField(default= False)
    isrecentproduct = models.CharField(choices=CATEGORY_OPTIONS, max_length=100)
    owner           = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, null=True)
    productcategoryID = models.ForeignKey(ProductsCategory, on_delete=models.DO_NOTHING)

    class Meta:
        ordering: ['-productUpdate']

    def __str__(self):
        return str(self.productName)

# class ProductImage(models.Model):
#     productID = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
#     images    = models.FileField(upload_to = 'productimages/')
#
#     def __str__(self):
#         return self.productID.productName
