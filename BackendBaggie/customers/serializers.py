from rest_framework import serializers
from customers.models import Customer
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

# Register
###################################################################
class RegisterCustomerSerializer(serializers.ModelSerializer):

	class Meta:
		model = Customer
		fields = ('id','username','mobile_number')

	# def validate(self, attrs):
	# 	mobile_number = attrs.get('mobile_number', '')
	# 	username = attrs.get('username', '')
	def create(self, validated_data):
		return Customer.objects.create(**validated_data)

########################################################################
#Login with Mobile Number
#######################################################################
class LoginCustomerSerializer(serializers.ModelSerializer):
	mobile_number = serializers.CharField(max_length= 15)
	username = serializers.CharField(
		max_length=255, min_length=3, read_only=True)
	tokens = serializers.CharField(max_length=68, min_length=6, read_only=True)

	class Meta:
		model = Customer
		fields = ('mobile_number','username', 'tokens')

	def validate(self, attrs):
		mobile_number = attrs.get('mobile_number', '')
		#print(mobile_number)
		#password = attrs.get('password', '')
		user = Customer.objects.get(mobile_number = mobile_number)
		#print(user.email)

		#user = auth.authenticate(mobile_number=mobile_number)
		#print(user)
		if not user:
			raise AuthenticationFailed('Invalid credentials, try again')
		if not user.is_active:
			raise AuthenticationFailed('Account disabled, contact admin')
		#if not user.is_verified:
		#	raise AuthenticationFailed('Email is not verified')

		return {
			'mobile_number':user.mobile_number,
			'username': user.username,
			'tokens': user.tokens
		}

		return super().validate(attrs)
