from orders.models import Order
from orders.serializers import OrderSerializer
from permissions import IsOwner
from headers import *
# Create your views here.

from rest_framework.permissions import SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions


class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        print("request.user", request.user)
        print("obj.owner",obj.owner)

        if request.method in SAFE_METHODS:
            return True

        return obj.owner == request.user

class OrderListAPIView(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,PostUserWritePermission)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,PostUserWritePermission)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = "id"

    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)
