from django.db import models


class Manufacturer(models.Model):
    name = models.TextField(unique=True)
    logo = models.ImageField(upload_to='manufacturer', default="/media/manufacturer/default.png")
    url = models.TextField()

class Model(models.Model):
    name = models.TextField(unique=True)
    manufacturer = models.ForeignKey(Manufacturer, related_name='models', on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='variant', default='/media/variant/default.png')

class Variant(models.Model):
    name = models.TextField(unique=True)
    model = models.ForeignKey(Model, related_name='variants', on_delete=models.CASCADE)
    price = models.FloatField()