from operator import mod
from django.db import models

# Create your models here.


class ImgServe(models.Model):
    imgFile = models.ImageField(upload_to="")
