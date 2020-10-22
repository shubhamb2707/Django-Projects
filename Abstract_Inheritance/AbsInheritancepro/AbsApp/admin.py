from django.contrib import admin
from .models import Customer, Staff
class CustomerAdmin(admin.ModelAdmin):
	list_display = ["name", "address", "phone"]

class StaffAdmin(admin.ModelAdmin):
	list_display=["name", "address", "position"]


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Staff,StaffAdmin)