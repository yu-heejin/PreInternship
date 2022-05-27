from operator import mod
from django.db import models

# Create your models here.

class TestImage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) 
    name = models.CharField(max_length=255)
    # imgUrl = models.CharField(max_length=500)
    photo = models.FileField()

    def __str__(self):
        return self.name

# class Image(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)  
#     name = models.CharField(max_length=255)  
#     imgUrl = models.CharField(max_length=500)

#     def __str__(self):
#         return self.name
