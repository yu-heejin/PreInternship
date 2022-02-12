import imp
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from jdb.models import Img
from jdb.serializers import ImgSerializer

from django.core.files.storage import default_storage
# Create your views here.


@csrf_exempt
def ImgApi(request, id=0):
    if request.method == 'GET':
        imgs = Img.objects.all()
        imgs_serializer = ImgSerializer(imgs, many=True)
        return JsonResponse(imgs_serializer.data, safe=False)
# we are making use of serializer class to convert it into json format
    elif request.method == 'POST':
        img_data = JSONParser().parse(request)
        imgs_serializer = ImgSerializer(data=img_data)
        if imgs_serializer.is_valid():
            imgs_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        img_data = JSONParser().parse(request)
        img = Img.objects.get(id=img_data['id'])
        imgs_serializer = ImgSerializer(img, data=img_data)
        if imgs_serializer.is_valid():
            imgs_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        img = Img.objects.get(id=id)
        img.delete()
        return JsonResponse("Deleted Successfully", safe=False)


'''
@csrf_exempt
def savefile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)

'''
