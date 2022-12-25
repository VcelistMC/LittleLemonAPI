from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    basePrice = models.DecimalField(decimal_places=2, max_digits=4)
    stock = models.IntegerField(max_length=3)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)