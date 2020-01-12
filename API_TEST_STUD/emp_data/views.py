from django.shortcuts import render
from . models import Employee

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from . serializers import EmployeeSerializers
from rest_framework.response import Response
# Create your views here.

class employeeList(APIView):

	def get(self,req):

		employee = Employee.objects.all() # get all fields 
		serializr= EmployeeSerializers(employee, many=True) # convert to json
		return Response(serializr.data) #return json object to client

