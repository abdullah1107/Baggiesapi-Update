from django.db import models
from django.utils.translation import ugettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.
class Customer(models.Model):
	username      = models.CharField(max_length=255, db_index=True)
	email         = models.EmailField(verbose_name = "email", max_length = 35, unique =False)
	firstName     = models.CharField(max_length = 50, null=True)
	lastName      = models.CharField(max_length = 50, null = True)
	mobile_number = models.CharField(max_length= 15, unique=True)
	profileImage  = models.ImageField(upload_to='profiles/', null=True)
	varificationNumber = models.CharField(null=True, max_length=350)
	is_verified   = models.BooleanField(default=True)
	is_active     = models.BooleanField(default=True)
	provider      = models.CharField(max_length=25, null=True)
	def __str__(self):
		return self.mobile_number

	def tokens(self):
		refresh = RefreshToken.for_user(self)
		return{
			'refresh': str(refresh),
			'access': str(refresh.access_token)
		}
