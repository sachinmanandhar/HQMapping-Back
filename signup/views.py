from django.shortcuts import render
from rest_framework import viewsets, permissions          # add this
from .serializers import SignUpFormSerializer, UserLoginSerializer      # add this
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SignUp
import datetime
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny		



class TryFormView(viewsets.ModelViewSet):       # add this
    serializer_class = SignUpFormSerializer          # add this
    queryset = SignUp.objects.all()
# Create your views here.

class signupformAPI(APIView):
	def get(self,request):
		formData=SignUp.objects.all()
		serializer=SignUpFormSerializer(formData,many=True)
		return Response(serializer.data)
		
	def post(self,request):
		data_Serializer1 = SignUpFormSerializer(data=request.data)
		if data_Serializer1.is_valid():
			data_Serializer1.save()
			return Response(data_Serializer1.data,status=status.HTTP_201_CREATED)
		return Response({'key': 'value'})
		
class UserLogin(APIView):
	permissions_classes = [AllowAny]
	
	def post(self,request):
		serializer=UserLoginSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			new_data=serializer.data
			return Response(new_data, status=status.HTTP_200_OK)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
	
		
	
	



