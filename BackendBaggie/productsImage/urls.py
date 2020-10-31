from django.urls import path
from productsImage.views import ProductImageListAPIView, ProductImageDetailAPIView


urlpatterns = [
    path('', ProductImageListAPIView.as_view(), name = "ProductImageList"),
    path('<int:id>', ProductImageDetailAPIView.as_view(), name = "ProductImageDetails"),
]
