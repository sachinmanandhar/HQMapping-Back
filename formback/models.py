from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Form(models.Model):
	Province=models.CharField(max_length=100,null=False)
	District=models.CharField(max_length=100,null=False)
	PalikaType=models.CharField(max_length=100,null=False)
	PalikaName=models.CharField(max_length=100,null=False)
	Ward_No=models.CharField(max_length=100,null=False)
	Ward_Office_Address=models.CharField(max_length=100,null=False)
	Ward_Contact_No=PhoneNumberField()
	X_Cords=models.FloatField(null=False)	
	Y_Cords=models.FloatField(null=False)
	Chairperson_Name=models.CharField(max_length=100,null=False)
	Chaiperson_Contact_No=PhoneNumberField()
	Secretary_Name=models.CharField(max_length=100,null=False)
	Secretary_Contact_No=PhoneNumberField()
	Area=models.FloatField(max_length=100,null=False)
	Total_Households=models.IntegerField(null=False)
	Total_Population=models.IntegerField(null=False)
	Total_Male_Population=models.IntegerField(null=False)
	Total_Female_Population=models.IntegerField(null=False)
	Website= models.URLField(max_length=200)
	Email=models.EmailField(max_length=254)
	location= models.PointField(srid=4326)
def __str__(self):
    return 'PalikaName: %s' % self.name

class TryForm(models.Model):
	enteredArea=models.CharField(max_length=100,null=False)
	enteredChaiPersonContact=models.CharField(max_length=100,null=False)
	enteredChairPersonName=models.CharField(max_length=100,null=False)
	enteredEmail=models.CharField(max_length=100,null=False)
	enteredFemalePop=models.CharField(max_length=100,null=False)
	enteredHouseholds=models.CharField(max_length=100,null=False)
	enteredMalePop=models.CharField(max_length=100,null=False)
	enteredPalikaName=models.CharField(max_length=100,null=False)
	enteredSecretaryContact=models.CharField(max_length=100,null=False)
	enteredSecretaryName=models.CharField(max_length=100,null=False)
	enteredTotalPop=models.CharField(max_length=100,null=False)
	enteredWardContactNo=models.CharField(max_length=100,null=False)
	enteredWardNo=models.CharField(max_length=100,null=False)
	enteredWardOfficeAddress=models.CharField(max_length=100,null=False)
	enteredWebsite=models.CharField(max_length=100,null=False)
	enteredXCords=models.CharField(max_length=100,null=False)
	enteredYCords=models.CharField(max_length=100,null=False)
	selectedDistrict=models.CharField(max_length=100,null=False)
	selectedPalikaType=models.CharField(max_length=100,null=False)
	selectedPro=models.CharField(max_length=100,null=False)

	
	
	
	
	
	
	
	
	
	
	
	
