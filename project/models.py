from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=100)

class ShoeType(models.Model):
    style = models.CharField(max_length=75)

class ShoeColor(models.Model):
    color_name = models.CharField(max_length=75)

class Shoe(models.Model):
    size = models.IntegerField(max_length=2)
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=100)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=40)