from django.db import models

# Create your models here.

class Banner1(models.Model):
    title = models.CharField(max_length=251,default="ninguno")
    title_color = models.CharField(max_length=251,default="#ffffff")
    title_2 = models.CharField(max_length=251,default="ninguno")
    title_color_2 = models.CharField(max_length=251,default="#ffffff")
    title_3 = models.CharField(max_length=251,default="ninguno")
    title_color_3 = models.CharField(max_length=251,default="#ffffff")
    subtitle = models.CharField(max_length=251,default=False)
    subtitle_color = models.CharField(max_length=251,default="#ffffff")
    subtitle_2 = models.CharField(max_length=251,default=False)
    subtitle_color_2 = models.CharField(max_length=251,default="#ffffff")
    subtitle_3 = models.CharField(max_length=251,default=False)
    subtitle_color_3 = models.CharField(max_length=251,default="#ffffff")
    banner = models.ImageField(upload_to="banner")
    banner_2 = models.ImageField(upload_to="banner",default=False)
    banner_3 = models.ImageField(upload_to="banner",default=False)
    status = models.BooleanField(default=False)
    status_2 = models.BooleanField(default=False)
    status_3 = models.BooleanField(default=False)
    login_image = models.ImageField(upload_to="login_image",default=False)






