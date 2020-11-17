from products.models import Products
from products.serializers import ProductsSerializer
from headers import *
from products.permissions import CanEditPermissionForProducts
from rest_framework.filters import SearchFilter, OrderingFilter

class ProductsListAPIView(ListCreateAPIView):
	permission_classes = (CanEditPermissionForProducts,)
	__basic_fields = ('productname','productpriceoriginal','productUpdate','isrecentproduct','vendorID__vandorName','productcategoryID__categoryName')
	serializer_class = ProductsSerializer
	queryset = Products.objects.all()
	filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)

	filter_fields = __basic_fields
	search_fields = __basic_fields

class ProductsDetailAPIView(RetrieveUpdateDestroyAPIView):
	permission_classes = (permissions.IsAuthenticated,CanEditPermissionForProducts,)
	serializer_class = ProductsSerializer
	queryset = Products.objects.all()
	lookup_field = "id"

	# def get_queryset(self):
	#     return self.queryset.filter(owner=self.request.user)
