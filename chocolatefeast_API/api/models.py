from typing import Any
from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50)


class Promotion(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=244)
    wraps = models.PositiveIntegerField()


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    stores = models.ManyToManyField(Store)
    promotions = models.ManyToManyField(Promotion)


class Client(models.Model):
    name = models.CharField(max_length=50)
    budget = models.PositiveIntegerField()


class Order(models.Model):
    quantity = models.PositiveIntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
