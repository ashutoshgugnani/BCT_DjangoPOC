from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200, blank=False, default='')
    price = models.IntegerField(blank=False, default='')
    category = models.CharField(max_length=200,blank=False, default='')
