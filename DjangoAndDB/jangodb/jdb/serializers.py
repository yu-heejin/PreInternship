from rest_framework import serializers
from jdb.models import Img


class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img
        fields = '__all__'
