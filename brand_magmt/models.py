from django.db import models

# Create your models here.


class Registerpage(models.Model):
    bname = models.CharField(max_length=40, null=True)
    bemail = models.CharField(max_length=40, null=True)
    password = models.CharField(max_length=40, null=True)
    logo = models.ImageField(null=True, blank=True)
    certificate = models.CharField(max_length=40, null=True,blank=True)

    
    def __str__(self):
        return self.bname



class Product(models.Model):
    CATEGORY =(
        ('mens','mens'),
        ('womens','womens'),
        ('kids-boys','kids-boys'),
        ('kids-girls','kids-girls')
    )
    brand= models.CharField(max_length=40, null=True)
    name = models.CharField(max_length=40, null=True)
    designer = models.CharField(max_length=40, null=True)
    ratings = models.CharField(max_length=40, null=True)
    quantity = models.CharField(max_length=40,null=True)
    price = models.CharField(max_length=40,null=True)
    images = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=250,null=True)
    category = models.CharField(max_length=40,null=True,choices=CATEGORY)
    date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    size = models.CharField(max_length=40,null=True)


    def __str__(self):
        return self.name



class Designer(models.Model):
    name = models.CharField(max_length=100,null= True, blank=True)
    designation = models.CharField(max_length=100,null= True, blank=True)
    email = models.CharField(max_length=100,null= True, blank=True)
    phone = models.CharField(max_length=10, null= True, blank=True)
    images = models.ImageField(null=True, blank=True)
    facebook = models.URLField(max_length=100,null= True, blank=True)
    insta = models.URLField(max_length=100,null= True, blank=True)

    def __str__(self):
        return self.name

