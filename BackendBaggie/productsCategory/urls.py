from django.urls import path
#from productsCategory.views import ProductsCategoryListAPIView, ProductsCategoryDetailAPIView
from productsCategory.views import(
    ProductsCategoryListAPIView,
    #ProductsCategorycreateAPIView,
    # api_update_productCategory_view,
    # api_create_productCategory_view,
    # api_delete_productCategory_view,
    ProductsCategoryDetailAPIView,

)
app_name = "productsCategory"
urlpatterns = [
     path('', ProductsCategoryListAPIView.as_view(), name = "List"),
     #path('create/', ProductsCategorycreateAPIView.as_view(), name = "create"),
     path('<int:id>', ProductsCategoryDetailAPIView.as_view(), name = "pCategoryDetails"),
    # #path('create/', ProductscategoryCreateView.as_view(), name='create'),
    #  path('create/', api_create_productCategory_view, name="create"),
    #  path('update/<int:pk>', api_update_productCategory_view, name="update"),
    #  path('delete/<int:pk>', api_delete_productCategory_view, name="delete"),
]
