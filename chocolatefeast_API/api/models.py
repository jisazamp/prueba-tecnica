from django.db import models

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    stores = models.ManyToManyField(Store)


class Client(models.Model):
    name = models.CharField(max_length=50)
    budget = models.PositiveIntegerField()


class Order(models.Model):
    quantity = models.PositiveIntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
