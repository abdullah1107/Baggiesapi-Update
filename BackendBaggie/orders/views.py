from orders.models import Order
from orders.serializers import OrderSerializer
from permissions import IsOwner
from headers import *
# Create your views here.

from orderDetails.models import *
from orderDetails.serializers import *
from orders.models import *
from orders.serializers import *
from headers import *

# class PostUserWritePermission(BasePermission):
#     message = 'Editing posts is restricted to the author only.'
#
#     def has_object_permission(self, request, view, obj):
#
#         if request.method in SAFE_METHODS:
#             return True
#
#         return obj.owner == request.user

class OrderListAPIView(ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,PostUserWritePermission)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "id"

    # @action(detail=True, methods=["GET"])
    # def choices(self, request, id=None):
    #     order = self.get_object()
    #     choices = OrderDetails.objects.filter(order=order)
    #     serializer = OrderDetailsSerializer(choices, many=True)
    #     return Response(serializer.data, status=200)
    #
    # @action(detail=True, methods=["POST"])
    # def choice(self, request, id=None):
    #     order = self.get_object()
    #     data = request.data
    #     data["order"] = order.id
    #     serializer = OrderDetailsSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.erros, status=400)


class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,PostUserWritePermission)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = "id"

    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)
