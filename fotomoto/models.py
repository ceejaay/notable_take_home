from django.db import models

# Create your models here.


class Images(models.Model):
    url = models.CharField(max_length=256)
    for_sale = models.BooleanField()
