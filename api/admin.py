from django.contrib import admin

from . models import Item, Location, Stock

admin.site.register(Item)
admin.site.register(Location)
admin.site.register(Stock)