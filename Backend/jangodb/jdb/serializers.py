from rest_framework import serializers
from jdb.models import Img


class ImgSerializer(serializers.ModelSerializer):
    imgUrl = serializers.FileField(use_url=False)

    class Meta:
        model = Img
        fields = '__all__'
