from django.urls import path
from orders.views import *
#
urlpatterns = [
    path('api/v1/', OrderListAPIView.as_view(), name = "odersList"),
    path('api/v1/<int:id>', OrderDetailAPIView.as_view(), name = "ordersDetails"),
]
