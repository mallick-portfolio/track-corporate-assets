from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from account.models import CustomUser
import traceback
from .serializers import (
  CompanySerializer,
  EmployeeSerializer,
  CreateEmployeeSerializer,
  DeviceSerializer,
  AllocationDeviceSerializer
  ,DeviceConditionLogSerializer
  )
from .models import Employee, Company, Device, AllocationDevice, DeviceConditionLog
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
          'message': "Employeee retrive successfully!!!",
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
          'message': "Failed to added employee!!!",
          'error': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response({
          "error": f'Error is {e}',
          'trackback': "".join(traceback.format_exception(type(e), e, e.__traceback__))
          })
class DeviceAPIView(APIView):
  permission_classes = [IsAuthenticated]
  def get(self, request):
    try:
      user = request.user
      company = Company.objects.filter(owner=user).first()
      if company is not None:
        device = Device.objects.filter(company=company)
        data = DeviceSerializer(device, many=True).data
        return Response({
          "success": True,
          'message': "Devices retrive successfully!!!",
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
      serializer = DeviceSerializer(data=data)
      if serializer.is_valid():
        serializer.save()
        return Response({
          "success": True,
          'message': "Device added successfully!!!",
          'data': serializer.data
        }, status=status.HTTP_200_OK)
      else:
        return Response({
          "success": True,
          'message': "Failed to add device!!!",
          'error': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response({
          "error": f'Error is {e}',
          'trackback': "".join(traceback.format_exception(type(e), e, e.__traceback__))
          })


class AllocationDeviceAPIView(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request):
    try:
      data = request.data
      allocationDevice = AllocationDevice.objects.filter(device=data['device'], employee=data['employee']).first()
      if allocationDevice is not None:
        return Response({
          "success": True,
          'message': "This device is allocated you already!!!",
        }, status=status.HTTP_400_BAD_REQUEST)

      else:
        serializer = AllocationDeviceSerializer(data=data)
        if serializer.is_valid():
          serializer.save()
          return Response({
            "success": True,
            'message': "Device allocate successfully!!!",
            'data': serializer.data
          }, status=status.HTTP_200_OK)
        else:
          return Response({
            "success": True,
            'message': "Failed to allocate device!!!",
            'error': serializer.errors
          }, status=status.HTTP_400_BAD_REQUEST)


    except Exception as e:
      return Response({
          "error": f'Error is {e}',
          'trackback': "".join(traceback.format_exception(type(e), e, e.__traceback__))
          })
class ReturnDeviceAPIView(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request):
    try:
      data = request.data
      user = request.user
      employee = Employee.objects.filter(user=user).first()
      device = Device.objects.filter(id=data['device']).first()

      if employee is not None and device is not None:
        DeviceConditionLog.objects.create(condition=data['condition'], device=device, employee=employee)

        return Response({
              "success": True,
              'message': "Device return successfully !!!",
            }, status=status.HTTP_200_OK)
      else:
        return Response({
              "success": True,
              'message': "Device return failed !!!",
            }, status=status.HTTP_400_BAD_REQUEST)


    except Exception as e:
      return Response({
          "error": f'Error is {e}',
          'trackback': "".join(traceback.format_exception(type(e), e, e.__traceback__))
          })