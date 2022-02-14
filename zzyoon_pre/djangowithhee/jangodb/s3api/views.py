from django.shortcuts import render
from rest_framework import viewsets, parsers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt

#######0213 오후 11시 40분까지 한 애들#########
# 낮까지 한 건 1로 올렸고 그 이후부터 django-s3direct까지 있는 코드~
# 다 에러있음 


# Create your views here.

# class DropBoxViewset(viewsets.ModelViewSet):
 
#     queryset = DropBox.objects.all()
#     serializer_class = DropBoxSerializer
#     parser_classes = [parsers.MultiPartParser, parsers.FormParser]
#     http_method_names = ['get', 'post', 'patch', 'delete']

class Image(APIView):

    @csrf_exempt
    def post(self, request, format=None):
        serializers = PhotoSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# from django.http import HttpResponseRedirect
# from django.shortcuts import get_object_or_404
# from rest_framework import generics, status, views
# from rest_framework.response import Response
# from django.urls import reverse
# from s3api.models import UploadedFile
# from s3api.serializers import UploadedFileSerializer, AccessControlListSerializer


# class UploadedFileCreateView(generics.CreateAPIView):
#     serializer_class = UploadedFileSerializer

#     def get_queryset(self):
#         return UploadedFile.objects.filter(user=self.request.user)

#     def create(self, request, *args, **kwargs):
#         acl_serialiser = AccessControlListSerializer(data=request.data)
#         acl_serialiser.is_valid(raise_exception=True)
#         file_serializer = self.get_serializer(
#             data={**request.data, 'user': request.user.id}
#         )
#         file_serializer.is_valid(raise_exception=True)
#         self.perform_create(file_serializer)
#         headers = self.get_success_headers(file_serializer.data)
#         uploaded_file = file_serializer.instance
#         uploaded_file_data = UploadedFileSerializer(instance=uploaded_file).data
#         uploaded_file_data['upload_form'] = uploaded_file.get_upload_form(
#             acl_type=acl_serialiser.validated_data['acl']
#         )
#         uploaded_file_data['complete_url'] = request.build_absolute_uri(
#             reverse('s3api:upload-file-complete', args=(str(uploaded_file.id),))
#         )
#         return Response(uploaded_file_data, status=status.HTTP_201_CREATED, headers=headers)


# class UploadedFileUploadCompleteView(views.APIView):
#     def post(self, request, file_id):
#         uploaded_file = get_object_or_404(
#             UploadedFile,
#             id=file_id,
#             file_upload_state=UploadedFile.UPLOAD_STATES.AWAIT_COMPLETE
#         )
#         uploaded_file.completed_upload()
#         return Response({
#             'status': UploadedFile.UPLOAD_STATES.COMPLETED
#         })


# class UploadedFileFetchView(views.APIView):
#     def get(self, request, file_id):
#         uploaded_file = get_object_or_404(
#             UploadedFile,
#             id=file_id
#         )
#         return HttpResponseRedirect(uploaded_file.get_download_url())

# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.parsers import MultiPartParser
# from datetime import datetime
# from boto3.session import Session
# import os
# import environ

# from .serializers import FileSerializer

# env = environ.Env(DEBUG=(bool, False))
# environ.Env.read_env()


# class FileUploadView(generics.GenericAPIView):

#     serializer_class = FileSerializer
#     parser_classes = (MultiPartParser, )

#     def get(self, request):
#         # do some "get or create" stuff
#         return "some data"


#     def post(self, request, format=None):
#         serializer = self.get_serializer(data=request.FILES)
#         serializer.is_valid(raise_exception=True)

#         file_extension = os.path.splitext(str(request.FILES['file']))[1]
#         filename = datetime.now().strftime("%d-%m-%YT%H:%M:%S") + file_extension
#         session = Session(region_name=env('REGION_NAME'),
#                           aws_access_key_id=env('AWS_ACCESS_KEY_ID'),
#                           aws_secret_access_key=env('AWS_SECRET_ACCESS_KEY'))
#         s3 = session.resource('s3')
#         s3.Bucket(env('BUCKET')).put_object(Key=filename, Body=request.FILES['file'])

#         return Response({"message": "Upload Successful"}, status=status.HTTP_200_OK)

# import json
# from datetime import datetime
# from django.conf import settings
# from django.http import (HttpResponse, HttpResponseBadRequest,
#                          HttpResponseForbidden, HttpResponseNotFound,
#                          HttpResponseServerError)
# from django.views.decorators.csrf import csrf_protect
# from django.views.decorators.http import require_POST
# try:
#     from urllib.parse import unquote
# except ImportError:
#     from urlparse import unquote
# from .utils import (get_aws_credentials, get_aws_v4_signature,
#                     get_aws_v4_signing_key, get_s3direct_destinations, get_key)

# @csrf_protect
# @require_POST
# def get_upload_params(request):
#     """Authorises user and validates given file properties."""
#     file_name = request.POST['name']
#     file_type = request.POST['type']
#     file_size = int(request.POST['size'])

#     dest = get_s3direct_destinations().get(request.POST.get('dest', None),
#                                            None)
#     if not dest:
#         resp = json.dumps({'error': 'File destination does not exist.'})
#         return HttpResponseNotFound(resp, content_type='application/json')

#     auth = dest.get('auth')
#     if auth and not auth(request.user):
#         resp = json.dumps({'error': 'Permission denied.'})
#         return HttpResponseForbidden(resp, content_type='application/json')

#     allowed = dest.get('allowed')
#     if (allowed and file_type not in allowed) and allowed != '*':
#         resp = json.dumps({'error': 'Invalid file type (%s).' % file_type})
#         return HttpResponseBadRequest(resp, content_type='application/json')

#     cl_range = dest.get('content_length_range')
#     if (cl_range and not cl_range[0] <= file_size <= cl_range[1]):
#         msg = 'Invalid file size (must be between %s and %s bytes).'
#         resp = json.dumps({'error': (msg % cl_range)})
#         return HttpResponseBadRequest(resp, content_type='application/json')

#     key = dest.get('key')
#     if not key:
#         resp = json.dumps({'error': 'Missing destination path.'})
#         return HttpResponseServerError(resp, content_type='application/json')

#     bucket = dest.get('bucket',
#                       getattr(settings, 'AWS_STORAGE_BUCKET_NAME', None))
#     if not bucket:
#         resp = json.dumps({'error': 'S3 bucket config missing.'})
#         return HttpResponseServerError(resp, content_type='application/json')

#     region = dest.get('region', getattr(settings, 'AWS_S3_REGION_NAME', None))
#     if not region:
#         resp = json.dumps({'error': 'S3 region config missing.'})
#         return HttpResponseServerError(resp, content_type='application/json')

#     endpoint = dest.get('endpoint',
#                         getattr(settings, 'AWS_S3_ENDPOINT_URL', None))
#     if not endpoint:
#         resp = json.dumps({'error': 'S3 endpoint config missing.'})
#         return HttpResponseServerError(resp, content_type='application/json')

#     aws_credentials = get_aws_credentials()
#     if not aws_credentials.secret_key or not aws_credentials.access_key:
#         resp = json.dumps({'error': 'AWS credentials config missing.'})
#         return HttpResponseServerError(resp, content_type='application/json')

#     upload_data = {
#         'object_key':
#         get_key(key, file_name, dest),
#         'access_key_id':
#         aws_credentials.access_key,
#         'session_token':
#         aws_credentials.token,
#         'region':
#         region,
#         'bucket':
#         bucket,
#         'endpoint':
#         endpoint,
#         'acl':
#         dest.get('acl') or 'public-read',
#         'allow_existence_optimization':
#         dest.get('allow_existence_optimization', False)
#     }

#     optional_params = [
#         'content_disposition', 'cache_control', 'server_side_encryption'
#     ]

#     for optional_param in optional_params:
#         if optional_param in dest:
#             option = dest.get(optional_param)
#             if hasattr(option, '__call__'):
#                 upload_data[optional_param] = option(file_name)
#             else:
#                 upload_data[optional_param] = option

#     resp = json.dumps(upload_data)
#     return HttpResponse(resp, content_type='application/json')


