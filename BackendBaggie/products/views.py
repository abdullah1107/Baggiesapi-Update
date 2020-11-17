from products.models import Products
from products.serializers import ProductsSerializer
from products.permissions import IsOwner
from headers import *

class ProductsListAPIView(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    # filter_backends = (filters.DjangoFilterBackend,)
	# filter_fields = ('productName')
    #

    # def perform_create(self, serializer):
    #     return serializer.save(owner=self.request.user and request.user.is_staff)

    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)


class ProductsDetailAPIView(RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()
    lookup_field = "id"

    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)
