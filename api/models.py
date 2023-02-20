'''
En este modelo de datos, hemos creado tres clases: Location, Item y Stock. 
La clase Location tiene un único campo, locationName, que almacena el nombre de una ubicación. 
La clase Item tiene dos campos: itemName, que almacena el nombre de un artículo, y price, que almacena el precio del artículo.

La clase Stock tiene tres campos: quantity, que almacena la cantidad de un artículo en una ubicación determinada;
location, que es una clave foránea a la tabla Location; y item, que es una clave foránea a la tabla Item. 
La clase Stock también tiene una restricción de unicidad en las columnas location y item, lo que significa que no puede haber dos registros con la misma combinación de ubicación y artículo.
'''

from django.db import models

class Location(models.Model):
    locationName = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.locationName

class Item(models.Model):
    itemName = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
      
    def __str__(self):
        return self.itemName

class Stock(models.Model):
    quantity = models.PositiveIntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('location', 'item')
   

    def __str__(self):
        return f'{self.item.itemName} - {self.location.locationName}: {self.quantity}'
   


