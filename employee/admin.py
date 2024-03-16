from django.contrib import admin
from .models import Employee, Company, Device, AllocationDevice,DeviceConditionLog
# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Device)
admin.site.register(AllocationDevice)
admin.site.register(DeviceConditionLog)