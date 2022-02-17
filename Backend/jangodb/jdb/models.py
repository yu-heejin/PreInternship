from distutils.command.upload import upload
from importlib.metadata import files
from operator import mod
from django.db import models

# Create your models here.


class Img(models.Model):
    imgUrl = models.FileField(upload_to="")
