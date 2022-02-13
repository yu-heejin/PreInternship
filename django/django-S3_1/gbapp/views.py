from django.shortcuts import render

# 연습확인용
# from django.http import HttpResponse

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_api.models import Tutorial
# from rest_api.serializers import TutorialSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *

# Create your views here.



# class Image(APIView):
#     def post(self, request, format=None):
#         serializers = PhotoSerializer(data = request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def helloAPI(request):
    return Response("hello Ghibli")


# @api_view(['GET'])
@api_view(['POST'])
@csrf_exempt
def upload_image(request):
    image = request.FILES['image']
    file_name = request.POST.get('file_name')

    client_s3 = boto3.client(
        's3',
        aws_access_key_id = 'AKIAUAMQWAYESYLBKBBP',
        aws_secret_access_key= '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'
    )


    client_s3.upload_file(file_name, ExtraArgs={'ContentType': 'image/jpeg'})

    # url = f'{end_point}{bucket_name}/{file_name}'

    return Response({'success': True,
                     'message': "File has been uploaded",
                     'url': url
                     },
                    status=status.HTTP_200_OK)

