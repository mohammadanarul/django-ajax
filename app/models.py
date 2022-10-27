from statistics import mode
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pk']
