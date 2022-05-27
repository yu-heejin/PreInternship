from django.shortcuts import render
from rest_framework import viewsets, parsers
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from django.core.files.storage import default_storage

class DropBoxViewset(viewsets.ModelViewSet):
 
    queryset = DropBox.objects.all()
    serializer_class = DropBoxSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']
    




# @csrf_exempt
# def S3DBApi(request, id=0):
#     if request.method == 'GET':
#         imgs = S3DB.objects.all()
#         imgs_serializer = S3DBSerializer(imgs, many=True)
#         return JsonResponse(imgs_serializer.data, safe=False)
# # we are making use of serializer class to convert it into json format
#     elif request.method == 'POST':
#         img_data = JSONParser().parse(request)
#         imgs_serializer = S3DBSerializer(data=img_data)
#         if imgs_serializer.is_valid():
#             imgs_serializer.save()
#             return JsonResponse("Added Successfully", safe=False)
#         return JsonResponse("Failed to Add", safe=False)
#     elif request.method == 'PUT':
#         img_data = JSONParser().parse(request)
#         img = S3DB.objects.get(id=img_data['id'])
#         imgs_serializer = S3DBSerializer(img, data=img_data)
#         if imgs_serializer.is_valid():
#             imgs_serializer.save()
#             return JsonResponse("Update successfully", safe=False)
#         return JsonResponse("Failed to Update")
#     elif request.method == 'DELETE':
#         img = S3DB.objects.get(id=id)
#         img.delete()
#         return JsonResponse("Deleted Successfully", safe=False)