import django.contrib.auth.password_validation as validators
from rest_framework import serializers
from .models import Form,TryForm

class FormSerializer(serializers.ModelSerializer):
	class Meta:
		model = Form
		fields = '__all__'
		
class TryFormSerializer(serializers.ModelSerializer):
	class Meta:
		model = TryForm
		fields = '__all__'