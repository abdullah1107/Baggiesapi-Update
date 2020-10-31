from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls.static import static
from django.conf import settings

schema_view = get_schema_view(
    openapi.Info(
        title="Baggie API",
        default_version='v1',
        description="Testing",
        contact=openapi.Contact(email="muhmmad.cse11@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
     path('admin/', admin.site.urls),
     #path('accounts/', include('allauth.urls')),
     # Local apps #############################################################
     path('auth/', include('users.urls')),

     #productsCategory
     path('productCategory/', include('productsCategory.urls')),
     # #products
     # path('products/', include('products.urls')),
     #
     # path('orders/', include('orders.urls')),
     #
     # path('orderdetails/', include('orderDetails.urls')),
     #
     #
     # path('productImage/',include('productsImage.urls')),
    # path('api/auth/', include('rest_framework_social_oauth2.urls')),

    #path('auth_backends/', include('users.urls')),
    ##########################################################################
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),

    path('api/api.json/', schema_view.without_ui(cache_timeout=0),
         name='schema-swagger-ui'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





    #when you go to -> 127.0.0.1:8000/accounts/ then you can see the list of urls
    # User management

    #for token
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
