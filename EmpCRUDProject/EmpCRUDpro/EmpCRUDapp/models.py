from django.db import models
from django.contrib.auth.models import User
class EmployeeData(models.Model):
	fname = models.CharField(max_length = 30)
	lname = models.CharField(max_length = 30)
	salary = models.IntegerField()
	location = models.CharField(max_length = 100)
	
	def __str__(self):
		return self.fname

