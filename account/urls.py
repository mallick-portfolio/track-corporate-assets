from django.urls import path
from . import views


urlpatterns = [
  path('register/', views.RegistrationAPIView.as_view(), name="register"),
  path('login/', views.LoginAPIView.as_view(), name="login"),
  # path('logout/', views.LogoutAPIView.as_view(), name="logout"),
  # path('me/', views.MeAPIView.as_view(), name="me"),
  # path('update-password/', views.UpdatePassword.as_view(), name="update-password"),
  # path('active/<uid64>/<token>/', views.activate, name='activate'),
]