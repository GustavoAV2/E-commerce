from django.db import models


class Product(models.Model):
    name = models.CharField("name", max_length=100)
    price = models.DecimalField("price", decimal_places=2, max_digits=6)
    description = models.CharField("description", null=True, max_length=300)
    amount = models.IntegerField("amount")

    def serialize(self):
        return {
            "name": self.name,
            "email": self.price,
            "description": self.description,
            "password": self.amount,
        }


class User(models.Model):
    name = models.CharField("name", max_length=100)
    email = models.EmailField("e-mail", max_length=100)
    password = models.CharField("password", max_length=100)

    def serialize(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
        }
