from rest_framework import serializers
from .models import *

class DropBoxSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = DropBox
        fields = '__all__'

