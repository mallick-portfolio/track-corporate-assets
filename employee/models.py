from django.db import models
from account.models import CustomUser


class Company(models.Model):
  owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  name = models.CharField(max_length = 100)
  since_year = models.IntegerField()
  location  = models.CharField(max_length=255)
  about = models.TextField(blank=True, null=True)
class Employee(models.Model):
  DEPT_TYPE =  [
    ('Engineering', 'Engineering Department'),
    ('Product Management', 'Product Management Department'),
    ('Quality Assurance', 'Quality Assurance Department'),
    ('Design', 'Design Department'),
    ('Sales', 'Sales Department'),
    ('Marketing', 'Marketing Department'),
    ('Human Resources', 'Human Resources Department'),
    ('Finance', 'Finance Department'),
    ('Customer Support', 'Customer Support Department'),
    ('Operations', 'Operations Department'),
  ]

  department = models.CharField(max_length=100, choices=DEPT_TYPE, blank=True, null=True)
  company = models.ForeignKey(Company, on_delete=models.CASCADE)
  user = models.OneToOneField(CustomUser,  on_delete=models.CASCADE)
  join_date = models.DateTimeField(auto_now_add=True)


class Device(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    device_type = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    quantity = models.IntegerField

class AllocationDevice(models.Model):
   employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
   device = models.ForeignKey(Device, on_delete=models.CASCADE)
   checkout_date = models.DateTimeField(auto_now_add=True)
   return_date = models.DateTimeField(null=True, blank=True)

class DeviceConditionLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    condition = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)