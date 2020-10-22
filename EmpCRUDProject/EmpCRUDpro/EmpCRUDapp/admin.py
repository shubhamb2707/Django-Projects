from django.contrib import admin
from .models import EmployeeData

class AdminEmployee(admin.ModelAdmin):
	list_display = ["fname", "lname", "salary", "location"]
admin.site.register(EmployeeData,AdminEmployee)

