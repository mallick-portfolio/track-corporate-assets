from django.urls import path
from .views import (CompanyAPIView,
                    EmployeeAPIView,
                    DeviceAPIView,
                    AllocationDeviceAPIView,
                    ReturnDeviceAPIView
                    )


urlpatterns = [
    path("", EmployeeAPIView.as_view(), name="employee"),
    path("company/", CompanyAPIView.as_view(), name="company"),
    path("device/", DeviceAPIView.as_view(), name="device"),
    path("allocation-device/", AllocationDeviceAPIView.as_view(), name="allocate-device"),
    path("return-device/", ReturnDeviceAPIView.as_view(), name="return-device"),
]
