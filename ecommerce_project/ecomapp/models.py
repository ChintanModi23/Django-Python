from django.db import models

# Create your models here.
class Products(models.Model):

    ProductID = models.CharField(max_length=20)
    ProductName = models.CharField(max_length=20)
    Price = models.FloatField()
    ProductImage = models.ImageField()