from django.shortcuts import render
from rest_framework import viewsets # new
from customers.models import Customer
from customers.serializers import *
#from users.serializers import RegisterSerializer, SetNewPasswordSerializer, ResetPasswordEmailRequestSerializer, EmailVerificationSerializer, LoginSerializer,LoginwithPhoneSerializer
from users.utils import Util
from users.renderers import UserRenderer

from headers import *

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView


# Create your views here.

class RegisterCustomerView(generics.GenericAPIView):

    serializer_class = RegisterCustomerSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = Customer.objects.get(mobile_number=user_data['mobile_number'])
        token = RefreshToken.for_user(user)
        user_data ={
        "response":user_data,
        "refresh":str(token),
        "access": str(token.access_token),
        }
        # current_site = '127.0.0.1:8000'
        # #current_site = get_current_site(request).domain
        # relativeLink = reverse('email-verify')
        # absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        # email_body = 'Hi '+user.username + \
        #     ' Use the link below to verify your email \n' + absurl
        # data = {'email_body': email_body, 'to_email': user.email,
        #        'email_subject': 'Verify your email'}

        #Util.send_email(data)
        return Response(user_data,status=status.HTTP_201_CREATED)

class LoginCustomerAPIView(generics.GenericAPIView):
    serializer_class = LoginCustomerSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
