from django.db import models

# Create your models here.

class ImageUP(models.Model):
    name = models.CharField(max_length=60)
    img = models.FileField(max_length=30)
    def __str__(self):
        return self.name