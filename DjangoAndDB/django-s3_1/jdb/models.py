from operator import mod
from django.db import models

# Create your models here.


class Img(models.Model):
    imgUrl = models.CharField(max_length=500)
    imgFile = models.ImageField(upload_to='items', null=True)
