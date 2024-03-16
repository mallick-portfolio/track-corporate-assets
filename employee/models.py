from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class Employee(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = [
        ('user', 'user'),
        ('admin', 'admin'),
        # Add more choices as needed
    ]
    USER_TYPE_CHOICES = [
        ('user', 'user'),
        ('admin', 'admin'),
        # Add more choices as needed
    ]


    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')


    # user type
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')

    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email