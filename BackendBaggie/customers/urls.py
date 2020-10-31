from django.urls import path,include
from rest_framework.routers import SimpleRouter

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from customers.views import RegisterCustomerView,LoginCustomerAPIView


urlpatterns = [

    path('customer/register/', RegisterCustomerView.as_view(), name="register"),
    path('customer/login/', LoginCustomerAPIView.as_view(), name="login"),
    path('customer/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
