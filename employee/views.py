from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from account.models import CustomUser
import traceback
from .serializers import CompanySerializer, EmployeeSerializer,CreateEmployeeSerializer
from .models import Employee, Company
from rest_framework.permissions import IsAuthenticated



class CompanyAPIView(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request):
    try:
      data = request.data
      serializer = CompanySerializer(data=data)
      if serializer.is_valid():
        serializer.save()
        return Response({
          "success": True,
          'message': "Company created successfully!!!",
          'data': serializer.data
        }, status=status.HTTP_200_OK)
      else:
        return Response({
          "success": True,
          'message': "Failed to create compay!!!",
          'error': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response({
          "error": f'Error is {e}',
          'trackback': "".join(traceback.format_exception(type(e), e, e.__traceback__))
          })


class EmployeeAPIView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request):
    try:
      user = request.user
      company = Company.objects.filter(owner=user).first()
      print("companuy", company)
      if company is not None:
        employee = Employee.objects.filter(company=company)
        data = EmployeeSerializer(employee, many=True).data
        return Response({
          "success": True,
          'message': "Employeee added successfully!!!",
          'data': data
        }, status=status.HTTP_200_OK)

    except Exception as e:
      return Response({
          "error": f'Error is {e}',
          'trackback': "".join(traceback.format_exception(type(e), e, e.__traceback__))
          })


  def post(self, request):
    try:
      data = request.data
      serializer = CreateEmployeeSerializer(data=data)
      if serializer.is_valid():
        serializer.save()
        return Response({
          "success": True,
          'message': "Employeee added successfully!!!",
          'data': serializer.data
        }, status=status.HTTP_200_OK)
      else:
        return Response({
          "success": True,
          'message': "Failed to add employee!!!",
          'error': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response({
          "error": f'Error is {e}',
          'trackback': "".join(traceback.format_exception(type(e), e, e.__traceback__))
          })