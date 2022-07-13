from django.db import models


class Product (models.Model):
    name = models.CharField(max_length=200)
    Image = models.ImageField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}"


class User (models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


