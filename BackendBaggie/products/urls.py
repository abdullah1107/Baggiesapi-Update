from django.urls import path
from rest_framework.routers import SimpleRouter
from products.views import ProductsListAPIView,ProductsDetailAPIView
#
urlpatterns = [
    path('api/v1', ProductsListAPIView.as_view(), name = "productsList"),
    path('api/v1/<int:id>', ProductsDetailAPIView.as_view(), name = "productsDetails"),
]
