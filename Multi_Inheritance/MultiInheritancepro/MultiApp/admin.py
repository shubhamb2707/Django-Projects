from django.contrib import admin
from .models import Restaurants, Place


class PlaceAdmin(admin.ModelAdmin):
	list_display = ["name", "address"]



class RestaurantAdmin(admin.ModelAdmin):
	list_display = ["name", "address", "serves_pizza", "serves_coffee"]




admin.site.register(Place,PlaceAdmin)
admin.site.register(Restaurants,RestaurantAdmin)