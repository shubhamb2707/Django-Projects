from django.db import models
class ContactInfo(models.Model):
	name = models.CharField(max_length=50)
	address = models.TextField(max_length=100)

	class Meta:
		abstract = True 

class Customer(ContactInfo):
	phone = models.BigIntegerField()

class Staff(ContactInfo):
	position = models.CharField(max_length=100)
