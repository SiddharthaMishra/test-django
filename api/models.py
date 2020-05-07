from django.db import models


class Manufacturer(models.Model):
    name = models.TextField(unique=True)
    logo = models.ImageField(null=True)
    url = models.URLField()

class Model(models.Model):
    name = models.TextField(unique=True)
    manufacturer = models.ForeignKey(Manufacturer, related_name='models', on_delete=models.CASCADE)

class Varient(models.Model):
    name = models.TextField(unique=True)
    picture = models.ImageField(null=True)
    model = models.ForeignKey(Model, related_name='varients', on_delete=models.CASCADE)

    # dimensions in inches 
    width = models.FloatField()
    height = models.FloatField() 