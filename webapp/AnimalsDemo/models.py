from django.db import models

# Create your models here.

class Animals(models.Model):
    Name=models.CharField(max_length=200)
    Type=models.CharField(max_length=200)
    Colour=models.CharField(max_length=200)
    Size=models.IntegerField()