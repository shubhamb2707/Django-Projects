from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    mobile_number = models.CharField(max_length=10)
    birth_date = models.CharField(max_length=50, null=True, blank=True)