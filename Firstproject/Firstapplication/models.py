from django.db import models


# Create your models here.
class Students(models.Model):

    StudentID = models.CharField(max_length=20)
    Name = models.CharField(max_length=20)
    ContactNum = models.CharField(max_length=20)
    Address = models.CharField(max_length=50)