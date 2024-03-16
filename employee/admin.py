from django.contrib import admin
from .models import Employee, Company
# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)