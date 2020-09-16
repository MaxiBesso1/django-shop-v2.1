from django.db import models
from images.models import Images
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
    banner = models.ForeignKey(Images,on_delete=models.CASCADE,related_name="imagen1")
    banner_2 = models.ForeignKey(Images,on_delete=models.CASCADE,related_name="imagen2")
    banner_3 = models.ForeignKey(Images,on_delete=models.CASCADE,related_name="imagen3")
    status = models.BooleanField(default=False)
    status_2 = models.BooleanField(default=False)
    status_3 = models.BooleanField(default=False)
    login_image = models.ForeignKey(Images,on_delete=models.CASCADE,related_name="imagen4")





