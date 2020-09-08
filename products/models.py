from django.db import models
from .templatetags.control import get_categorys_as_tuple

CHOICES = get_categorys_as_tuple()
# Create your models here.
#Product model
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    description = models.TextField()
    category = models.CharField(max_length=250,default="Otros",choices=CHOICES)
    exact_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    date = models.DateField(auto_now=True)
    link = models.CharField(max_length=291)
    principal_image = models.ImageField(upload_to="products")
    banner_image1 = models.ImageField(upload_to="products")
    banner_image2 = models.ImageField(upload_to="products",blank=True)
    banner_image3 = models.ImageField(upload_to="products",blank=True)
    offer = models.BooleanField(default=False)
    new_price= models.FloatField(blank=True,null=True)




        