from django.urls import path
from .views import CompanyAPIView, EmployeeAPIView
urlpatterns = [
    path("", EmployeeAPIView.as_view(), name="employee"),
    path("company/", CompanyAPIView.as_view(), name="company"),
]
