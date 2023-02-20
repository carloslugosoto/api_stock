from rest_framework import serializers
from api.models import Location, Item, Stock

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Stock
        fields = '__all__'
