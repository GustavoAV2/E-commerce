from django.db import models


class User(models.Model):
    name = models.CharField("name", max_length=100)
    price = models.DecimalField("price", decimal_places=2, max_digits=6)
    amount = models.IntegerField("amount")


class Product(models.Model):
    name = models.CharField("name", max_length=100)

