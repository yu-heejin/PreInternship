'''
from urllib import request
from rest_framework.viewsets import ModelViewSet
from .models import ImgServe
from django.http.response import JsonResponse
from .serializer import ImgServeSerializer
from django.core.files.storage import FileSystemStorage
@method_decorator(csrf_exempt, name='dispatch')
def simple_upload(request):
    if request.method == 'POST':
        imgs_serializer = ImgServeSerializer(data=request.FILES)
        if imgs_serializer.is_valid():
            imgs_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
def ImgServApi(request):
    if request.method == 'GET':
        imgs = ImgServe.objects.all()
        imgs_serializer = ImgServeSerializer(imgs, many=True)
        return JsonResponse(imgs_serializer.data, safe=False)
class FileTestViewSet(ModelViewSet):
    queryset = ImgServe.objects.all()
    serializer_class = ImgServeSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializer import ImgServeSerializer
from .models import ImgServe

class FileTestViewSet(ModelViewSet):
    imgFile = ImgServe.objects.all()
    serializer_class = ImgServeSerializer
'''

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializer import ImgServeSerializer
from .models import ImgServe


class FileTestViewSet(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        imgs = ImgServe.objects.all()
        imgs_serializer = ImgServeSerializer(imgs, many=True)
        return Response(imgs_serializer.data)

    def post(self, request):
        file_serializer = ImgServeSerializer(data=request.FILES)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
