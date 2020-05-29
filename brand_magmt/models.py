from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=40, null=True)
    designer = models.CharField(max_length=40, null=True)
    ratings = models.CharField(max_length=40, null=True)
    quantity = models.CharField(max_length=40,null=True)
    price = models.CharField(max_length=40,null=True)
    description = models.CharField(max_length=250,null=True)
    category = models.CharField(max_length=40,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)


