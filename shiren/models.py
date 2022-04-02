from django.db import models

# Create your models here.

class Swords(models.Model):
    sword = models.CharField(max_length=256)
    type = models.CharField(max_length=256)

