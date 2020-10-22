from django.db import models
class Student(models.Model):
	student_id =  models.AutoField(primary_key = True)
	sname = models.CharField(max_length = 50)
	slocation = models.TextField(max_length = 100)
	marks = models.IntegerField()
    
    

class Customer(models.Model):
	customer_id = models.AutoField(primary_key = True)
	cname = models.CharField(max_length = 50)
	clocation = models.TextField(max_length = 100)
	sales = models.IntegerField()

	


class Employee(Student,Customer):
	ename = models.CharField(max_length = 50)
	elocation = models.TextField(max_length = 100)
	salary = models.IntegerField()
    
    