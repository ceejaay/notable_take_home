from django.db import models
# Create your models here.

class Swords(models.Model):
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=256)

class Prices(models.Model):
    price = models.IntegerField()

class Scrolls(models.Model):
    name = models.CharField(max_length=128)
    price_id = models.ForeignKey('prices', on_delete=models.CASCADE)

