from .serializers import RegistrationSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from account.models import CustomUser
import traceback
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from account.helpers import get_tokens_for_user



# register api
class RegistrationAPIView(APIView):
  def post(self, request):
    try:
      data = request.data
      serializer = RegistrationSerializer(data=data)
      if serializer.is_valid():
        serializer.save()
        return Response({
          "success": True,
          'message': "Registration successfull!!!."
        }, status=status.HTTP_201_CREATED)
      else:
        return Response({
          "success": False,
          'message': "Registration failed.Username or email already exist",
          'error': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
      return Response({
          "error": f'Error is {e}',
          'trackback': "".join(traceback.format_exception(type(e), e, e.__traceback__))
          })


# login api
class LoginAPIView(APIView):
  @csrf_exempt
  def post(self, request):
    try:
      rd = request.data
      if 'email' not in rd or 'password' not in rd:
        return Response({
          "success": False,
          'message': "Invalid Credentials",
        }, status=status.HTTP_400_BAD_REQUEST)


      email = rd['email']
      password = rd['password']
      user = authenticate(request, email=email, password=password)
      if user is not None:
        login(request, user=user)
        token = get_tokens_for_user(user)


        return Response({
          "success": True,
          "token": token,
          'message': "Login successfull!!!",
        }, status=status.HTTP_200_OK)
      else:
        return Response({
          "success": False,
          'message': "Failed to login. Invalid Credentials!!!",
          "error": True
        },status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
      return Response({'message':'fail','error':e,"status": status.HTTP_500_INTERNAL_SERVER_ERROR})


class LogoutAPIView(APIView):
  # permission_classes = [IsAuthenticated]
  # authentication_classes =[JWTAuthentication]
  @csrf_exempt
  def get(self, request):
    logout(request)
    return Response({
        "success": True,
        'message': "Successfully Logged out!!!",
        }, status=status.HTTP_200_OK)



class MeAPIView(APIView):
  permission_classes = [IsAuthenticated]
  authentication_classes =[JWTAuthentication]
  def get(self, request):
    try:
      user = CustomUser.objects.filter(id=request.user.id).first()
      if user is not None:
        data = UserSerializer(user).data
        return Response({
        "success": True,
        'message': "Profile retrive successfully",
        "data": data
        }, status=status.HTTP_200_OK)
      else:
        return Response({
        "success": False,
        'message': "User not found",
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
      return Response({
        "error": f'Error is {e}',
        'trackback': "".join(traceback.format_exception(type(e), e, e.__traceback__))
        })




  @csrf_exempt
  def put(self, request):
    try:
      user = CustomUser.objects.filter(id=request.user.id).first()
      if user is not None:
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
          serializer.save()
          return Response({
          "success": True,
          'message': "Profile updated successfully",
          "data": serializer.data
          }, status=status.HTTP_201_CREATED)
      else:
        return Response({
        "success": False,
        'message': "User not found",
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
      return Response({
        "error": f'Error is {e}',
        'trackback': "".join(traceback.format_exception(type(e), e, e.__traceback__))
        })