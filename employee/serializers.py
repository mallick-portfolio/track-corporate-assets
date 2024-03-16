from rest_framework import serializers
from employee.models import Company, Employee
from account.serializers import  CreateEmployeeWithUserSerializer
from account.models import CustomUser

class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = "__all__"

class CreateEmployeeSerializer(serializers.ModelSerializer):
  user = CreateEmployeeWithUserSerializer()
  class Meta:
    model = Employee
    fields = ['id', 'company', 'user', 'join_date', 'department']

  def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create_user(**user_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee


class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = '__all__'




