from django.urls import path
from orders.views import *
#
urlpatterns = [
    path('', OrderListAPIView.as_view(), name = "odersList"),
    path('<int:id>', OrderDetailAPIView.as_view(), name = "ordersDetails"),
]
