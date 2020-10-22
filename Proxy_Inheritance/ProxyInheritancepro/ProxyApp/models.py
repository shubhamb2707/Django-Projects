from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    location = models.TextField(max_length = 100)

    def __str__(self):
    	return self.first_name

class ProxyPerson(Person):
    class Meta:
        proxy = True

    def __str__(self):
    	return self.first_name.upper()


