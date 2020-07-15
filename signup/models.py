from django.contrib.gis.db import models

class SignUp(models.Model):
	Address=models.CharField(max_length=100,null=False)
	Email=models.CharField(max_length=100,null=False)
	Username=models.CharField(max_length=100,null=False)
	Password=models.CharField(max_length=100,null=False)
	
