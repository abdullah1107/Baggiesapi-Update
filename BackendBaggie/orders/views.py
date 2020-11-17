from orders.models import Order
from orders.serializers import OrderSerializer
from headers import *
from orders.permissions import CanCreatePermissionforCustomer


class OrderListAPIView(ListCreateAPIView):
    permission_classes = (CanCreatePermissionforCustomer,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (CanCreatePermissionforCustomer,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = "id"











## if loking for only method based then see ProductCategory

################################################################################
# when using only APIView
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




    # def get_queryset(self):
    #     return self.queryset.filter(owner=self.request.user)
