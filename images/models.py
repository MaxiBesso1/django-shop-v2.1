from django.db import models

# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=251)
    image = models.ImageField(upload_to="media/",blank=True,null=True)
    url = models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.name
