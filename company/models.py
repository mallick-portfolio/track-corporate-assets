from django.db import models

# Create your models here.

class Company(models.Model):
  name = models.CharField(max_length = 100)
  since_year = models.IntegerField()
  # location  = models.CharField()

