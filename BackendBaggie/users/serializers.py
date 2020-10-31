# from django.contrib.auth import get_user_model # new
from rest_framework import serializers
from users.models import CustomUser
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password


# class GoogleAuthSerializer(serializers.Serializer):
#     """
#     Handle serialization and deserialization of User objects
#     """
#
#     access_token = serializers.CharField()
#
#     def validate(self, data):
#         """
#         Handles validating a request and decoding and getting user's info
#         associated to an account on Google then authenticates the User
#         : params access_token:
#         : return: user_token
#         """
#         id_info = SocialValidation.google_auth_validation(
#             access_token=data.get('access_token'))
#         # check if data data retrieved once token decoded is empty
#         if not id_info:
#             raise serializers.ValidationError('token is not valid')
#
#         # check if a user exists after decoding the token in the payload
#         # the user_id confirms user existence since its a unique identifier
#
#         user_id = id_info['sub']
#
#         # query database to check if a user with the same email exists
#         user = CustomUser.objects.filter(email=id_info.get('email'))
#
#         # if the user exists,return the user token
#         if user:
#             return {
#                 'token': user[0].token,
#                 'user_exists': True,
#                 'message': 'Welcome back ' + id_info.get('name')
#             }
#
#         if id_info.get('picture'):
#             id_info['user_profile_picture'] = id_info['picture']
#
#         # pass user information to signal to be added to profile
#         # after user is created
#         SocialAuthProfileUpdate.get_user_info(id_info)
#
#         # create a new user if no new user exists
#         first_and_second_name = id_info.get('name').split()
#         first_name = first_and_second_name[0]
#         second_name = first_and_second_name[1]
#         payload = {
#             'email': id_info.get('email'),
#             'first_name': first_name,
#             'last_name': second_name,
#             'password': randomStringwithDigitsAndSymbols()
#         }
#
#         new_user = CustomUser.objects.create_user(**payload)
#         new_user.is_verified = True
#
#         new_user.social_id = user_id
#         new_user.save()
#
#         return {
#             'token': new_user.token,
#             'user_exists': False,
#             'message': 'Welcome to landville. ' + first_name +
#                        '. Ensure to edit your profile.'
#         }
###################################################################
#register a vendor
class RegisterVendonSerializer(serializers.ModelSerializer):
	password = serializers.CharField(
		max_length=68, min_length=6, write_only=True)

	class Meta:
		model = CustomUser
		fields = ('id','email','firstName','lastName','password', 'mobileNumber')

	def create(self, validated_data):
		return CustomUser.objects.create_vendoruser(**validated_data)

#register a customer
class RegisteCustomerSerializer(serializers.ModelSerializer):
	password = serializers.CharField(
		max_length=68, min_length=6, write_only=True)

	class Meta:
		model = CustomUser
		fields = ('id','name','email','mobileNumber','password')

	def create(self, validated_data):
		return CustomUser.objects.create_user(**validated_data)


# Login with Mobile Number
# ####################################################
#customer login
class LoginwithPhoneCustomerSerializer(serializers.ModelSerializer):
	mobileNumber = serializers.CharField(max_length= 15)

	email = serializers.EmailField(max_length=255, min_length=3, read_only=True)
	password = serializers.CharField(
		max_length=68, min_length=6, read_only=True)
	name = serializers.CharField(max_length=100, read_only=True)
	tokens = serializers.CharField(max_length=68, min_length=6, read_only=True)

	def get_tokens(self, obj):
		user = User.objects.get(mobileNumber=obj['mobileNumber'])
		return {
			'refresh': user.tokens()['refresh'],
			'access': user.tokens()['access']
		}

	class Meta:
		model = CustomUser
		fields = ('id', 'name','mobileNumber','email', 'password', 'tokens')

	def validate(self, attrs):
		mobileNumber = attrs.get('mobileNumber', '')

		user = CustomUser.objects.get(mobileNumber = mobileNumber)
		if not user:
			raise AuthenticationFailed('Invalid credentials, try again')
		if not user.is_active:
			raise AuthenticationFailed('Account disabled, contact admin')
		#if not user.is_verified:
		#	raise AuthenticationFailed('Email is not verified')

		return {
			'id':user.id,
			'mobileNumber':user.mobileNumber,
			'email': user.email,
			'name': user.name,
			'tokens': user.tokens
		}
		return super().validate(attrs)


# #Login with email and password
# ###############################################################
class LoginVendorSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(max_length=255, min_length=3)
	password = serializers.CharField(
		max_length=68, min_length=4, write_only=True)
	firstName = serializers.CharField(
		max_length=100, min_length=3, read_only=True)
	lastName = serializers.CharField(
		max_length=100, min_length=3, read_only=True)
	mobileNumber = serializers.CharField(
		max_length=15, read_only=True)
	tokens = serializers.CharField(max_length=68, min_length=6, read_only=True)

	def get_tokens(self, obj):
		user = CustomUser.objects.get(email=obj['email'])
		return {
			'refresh': user.tokens()['refresh'],
			'access': user.tokens()['access']
		}

	class Meta:
		model = CustomUser
		fields = ('id','email', 'firstName', 'lastName','password','mobileNumber','tokens')

	def validate(self, attrs):
		email = attrs.get('email', '')
		password = attrs.get('password', '')
		filtered_user_by_email = CustomUser.objects.filter(email=email)
		user = auth.authenticate(email=email, password=password)

		if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
			raise AuthenticationFailed(
				detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

		if not user:
			raise AuthenticationFailed('Invalid credentials, try again')
		if not user.is_active:
			raise AuthenticationFailed('Account disabled, contact admin')
		#if not user.is_verified:
		#	raise AuthenticationFailed('Email is not verified')

		return {
		    'id':user.id,
			'firstName':user.firstName,
			'lastName':user.lastName,
			'mobileNumber':user.mobileNumber,
			'email': user.email,
			'tokens': user.tokens
		}

		return super().validate(attrs)

#############################
#----> Email Verify
############################
class EmailVerificationSerializer(serializers.ModelSerializer):
	token = serializers.CharField(max_length=555)

	class Meta:
		model = CustomUser
		fields = ('token')



class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    #redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields = ('email')


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    token = serializers.CharField(
        min_length=1, write_only=True)
    uidb64 = serializers.CharField(
        min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)

            user.set_password(password)
            user.save()

            return (user)
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')
#
#
# ############## REset Password #####################
# class ResetPasswordEmailRequestSerializer(serializers.Serializer):
# 	email = serializers.EmailField(min_length=2)
#
# 	class Meta:
# 		fields = ('email')
#
# ############### SET NewPassword ############################
# class SetNewPasswordSerializer(serializers.Serializer):
# 	password = serializers.CharField(
# 		min_length=6, max_length=68, write_only=True)
# 	token = serializers.CharField(
# 		min_length=1, write_only=True)
# 	uidb64 = serializers.CharField(
# 		min_length=1, write_only=True)
#
# 	class Meta:
# 		fields = ('password', 'token', 'uidb64')
#
# 	def validate(self, attrs):
# 		try:
# 			password = attrs.get('password')
# 			token = attrs.get('token')
# 			uidb64 = attrs.get('uidb64')
#
# 			id = force_str(urlsafe_base64_decode(uidb64))
# 			user = CustomUser.objects.get(id=id)
# 			if not PasswordResetTokenGenerator().check_token(user, token):
# 				raise AuthenticationFailed('The reset link is invalid', 401)
#
# 			user.set_password(password)
# 			user.save()
#
# 			return (user)
# 		except Exception as e:
# 			raise AuthenticationFailed('The reset link is invalid', 401)
# 		return super().validate(attrs)
#
# class CustomUserSerilizer(serializers.ModelSerializer):
# 	class Meta:
# 		model  = CustomUser
# 		fields = ('id', 'username', 'email', 'mobileNumber')
