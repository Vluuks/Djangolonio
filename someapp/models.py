
from django.db import models
from datetime import datetime    

class Category(models.Model):
    description = models.CharField(max_length=1000)
    name = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.name}"

class User(models.Model):
    name = models.CharField(max_length=40)
    register_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categories")
    description = models.CharField(max_length=1000)
    name = models.CharField(max_length=40)
    inventory = models.IntegerField(default = 0)
    price = models.IntegerField(default = 0)
    # creation_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.id} - {self.name}"
