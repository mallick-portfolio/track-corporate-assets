from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = [
        ('Owner', 'Owner'),
        ('Employee', 'Employee'),
    ]
    GENDER_TYPE = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
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



    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE, default='Employee')
    department = models.CharField(max_length=100, choices=DEPT_TYPE)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email