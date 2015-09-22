from django.contrib import admin
from dujour.restaurants.models import Restaurant, DayRestaurant, Menu

# Register your models here.

class DayRestaurantInline(admin.TabularInline):
    model = DayRestaurant

class MenuInline (admin.TabularInline):
    model = Menu

class RestaurantAdmin(admin.ModelAdmin):
    inlines = [
        DayRestaurantInline,
        MenuInline
    ]

admin.site.register(Restaurant, RestaurantAdmin)
