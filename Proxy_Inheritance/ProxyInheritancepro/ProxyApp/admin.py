from django.contrib import admin
from .models import Person , ProxyPerson 


class AdminPerson(admin.ModelAdmin):
	list_display = ["first_name", "last_name", "location"]
class AdminProxy(admin.ModelAdmin):
	list_display = ["first_name", "last_name", "location"]


admin.site.register(Person, AdminPerson)
admin.site.register(ProxyPerson, AdminProxy)