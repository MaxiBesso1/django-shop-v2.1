from django.db import models
from images.models import Images

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=251)

    def __str__(self):
        return self.name

#Product model
class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    exact_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    date = models.DateField(auto_now=True)
    principal_image = models.ForeignKey(Images,on_delete=models.CASCADE,related_name="fotito")
    banner_images = models.ManyToManyField(Images,related_name="fotitos")
    offer = models.BooleanField(default=False)
    new_price= models.FloatField(blank=True,null=True)




        