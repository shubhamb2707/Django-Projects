from django.db import models

class Student(models.Model):
	sname=models.CharField(max_length=50)
	marks=models.IntegerField()
	college=models.CharField(max_length=50)

    