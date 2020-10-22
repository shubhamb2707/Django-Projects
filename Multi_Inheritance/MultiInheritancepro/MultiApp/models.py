from django.db import models
class Place(models.Model):
	name = models.CharField(max_length = 100)
	address = models.TextField(max_length = 100)


class Restaurants(Place):

	serves_pizza = models.BooleanField(default = False)
	serves_coffee = models.BooleanField(default = False)
   



