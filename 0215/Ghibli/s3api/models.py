from django.db import models

# Create your models here.
class DropBox(models.Model):
    name = models.CharField(max_length=30)
    photo = models.FileField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # s3_bucket_url = 'https://bucket-timmy.s3.ap-northeast-2.amazonaws.com/1.jpg'
    # mongodb로 보낼 s3 객체(이미지) url https://bucket-timmy.s3.ap-northeast-2.amazonaws.com/파일명.jpg
    # ;s3_bucket url =  
    # 'https://bucket-timmy.s3.ap-northeast-2.amazonaws.com/%s.jpg' %file_name 
    # 전송될 파일 url file:///data/user/0/com.cam3/cache/Camera/파일명.jpg
    # ; 'file:///data/user/0/com.cam3/cache/Camera/%s.jpg' %file_name
 
    class Meta:
        verbose_name_plural = 'Drop Boxes'

