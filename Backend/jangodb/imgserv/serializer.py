from rest_framework import serializers
from .models import ImgServe


class ImgServeSerializer(serializers.ModelSerializer):
    imgFile = serializers.ImageField(use_url=False)

    class Meta:
        model = ImgServe
        fields = '__all__'
