from django.shortcuts import render
from rest_framework import viewsets, permissions          # add this
from .serializers import FormSerializer,TryFormSerializer      # add this
from .models import Form,TryForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime

# Create your views here.
class FormView(viewsets.ModelViewSet):       # add this
	serializer_class = FormSerializer          # add this
	queryset = Form.objects.all() 
	permissions_classes=(permissions.IsAuthenticatedOrReadOnly,)
	
	
class TryFormView(viewsets.ModelViewSet):       # add this
	serializer_class = TryFormSerializer          # add this
	queryset = TryForm.objects.all()	
	permissions_classes=(permissions.IsAuthenticatedOrReadOnly,)
	
"""def InputForm(request):
	request.CONTENT_TYPE('application/json')
	request.REMOTE_ADDR('http://localhost:3000/')
	Fprov=request.POST.get('selectedPro')
	Fdist=request.POST.get('selectedDistrict')
	FpalikaT=request.POST.get('selectedPalikaType')
	FpalikaN=request.POST.get('enteredPalikaName')
	FWardN=request.POST.get('enteredWardNo')
	FWardOf=request.POST.get('enteredWardOfficeAddress')
	FWardC=request.POST.get('enteredWardContactNo')
	FX=float(request.POST.get('enteredXCords'))
	FY=float(request.POST.get('enteredYCords'))
	FChaipersonN=request.POST.get('enteredChairPersonName')
	FChairpersonC=request.POST.get('enteredChaiPersonContact')
	FSecN=request.POST.get('enteredSecretaryName')
	FSecC=request.POST.get('enteredSecretaryContact')
	FArea=request.POST.get('enteredArea')
	FHouseholds=request.POST.get('enteredHouseholds')
	FPop=request.POST.get('enteredTotalPop')
	FFepop=request.POST.get('enteredMalePop')
	Fmapop=request.POST.get('enteredFemalePop')
	FWeb=request.POST.get('enteredWebsite')
	FEmail=request.POST.get('enteredEmail')
	new=Form(Province=Fprov,
			 District=Fdist,
			 PalikaType=FpalikaT,
			 PalikaName=FpalikaN,
			 Ward_No=FWardN,
			 Ward_Office_Address=FWardOf,
			 Ward_Contact_No=FWardC,
			 X_Cords=FX,
			 Y_Cords=FY,
			 Chairperson_Name=FChaipersonN,
			 Chaiperson_Contact_No=FChairpersonC,
			 Secretary_Name=FSecN,
			 Secretary_Contact_No=FSecC,
			 Area=FArea,
			 Total_Households=FHouseholds,
			 Total_Population=FPop,
			 Total_Male_Population=Fmapop,
			 Total_Female_Population=FFepop,
			 Website=FWeb,
			 Email=FEmail,
			 location=Point(FX,FY, srid = 4326))
	form.save()
"""
	
class formAPI(APIView):
	def get(self,request):
		formData=TryForm.objects.all()
		serializer=TryFormSerializer(formData,many=True)
		return Response(serializer.data)
		
	def post(self,request):
		data_Serializer = TryFormSerializer(data=request.data)
		if data_Serializer.is_valid():
			data_Serializer.save()
			return Response({'PalikaName':data_Serializer.data.get('enteredPalikaName'),
							 'DateTime':datetime.datetime.now()},status=status.HTTP_201_CREATED)
		return Response({'key': 'value'})
	#permissions_classes=(permissions.IsAuthenticatedOrReadOnly,)
	
		
	
	
