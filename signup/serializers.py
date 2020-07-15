from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import SignUp
from django.db.models import Q
from rest_framework.serializers import (
	CharField,
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError)
	
Signup=get_user_model()
class SignUpFormSerializer(serializers.ModelSerializer):
	class Meta:
		model = SignUp
		fields = [
			'Address',
			'Email',
			'Username',
			'Password',
		
				]
		extra_kwargs={"Password":
							{"write_only:True"}
							}

class UserLoginSerializer(serializers.ModelSerializer):
	token=CharField(allow_blank=True, read_only=True)
	Username=CharField(required = False, allow_blank=True)
	Email=CharField(label='Email Address',required = False,allow_blank=True)
	class Meta:
		model = SignUp
		fields=[
			'Username',
			'Email',
			'Password',
			'token']
		extra_kwargs={"Password":
							{"write_only:True"}
					 }
	def validate(self,data):
		user_obj=None
		Email=data.get("Email",None)
		Username=data.get("Username",None)
		Password=data["Password"]
			
		if not Email and not Username:
			raise ValidationError("A Username or email is required to login")
		user = SignUp.objects.filter(
					Q(Email=Email) |
					Q(Username=Username)
				).distinct()
		if user.exists() and user.count() == 1:
			user_obj=user.first()
		else:
			raise ValidationError("this username/email is not valid.")
		if user_obj:
			if not user_obj.check_password(Password):
				raise ValidationError("Incorrect Password")
		data["token"]="Some Random Token"
		return data