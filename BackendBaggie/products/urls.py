from django.urls import path
from rest_framework.routers import SimpleRouter
from products.views import ProductsListAPIView,ProductsDetailAPIView
#
urlpatterns = [
    path('', ProductsListAPIView.as_view(), name = "productsList"),
    path('<int:id>', ProductsDetailAPIView.as_view(), name = "productsDetails"),
]
