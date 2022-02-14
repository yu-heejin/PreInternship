from rest_framework.routers import SimpleRouter
from django.urls import path, include, re_path
from .views import *
from s3api import views

# router = SimpleRouter()
# router.register('accounts', DropBoxViewset)
# urlpatterns = router.urls

urlpatterns = [
    path('image', views.Image.as_view(), name = 'image'),
    # path('image/<int:pk>/', Image.as_view()),
]

# from django.urls import path, include, re_path
# from s3api import views


# app_name = 's3api'


# urlpatterns = [
#     re_path(r'^$', view=views.UploadedFileCreateView.as_view(), name='upload-file-create'),
#     re_path(r'^(?P<file_id>[0-9a-f-]+)/$', view=views.UploadedFileFetchView.as_view(), name='upload-file-fetch'),
#     re_path(r'^(?P<file_id>[0-9a-f-]+)/complete/$', view=views.UploadedFileUploadCompleteView.as_view(), name='upload-file-complete'),
# ]

# from .views import FileUploadView

# urlpatterns = [
#     path('file-s3/', FileUploadView.as_view(), name='upload-to-s3'),
# ]

# urlpatterns = [
#     path('get_upload_params/', get_upload_params, name='s3direct'),
#     # path('get_aws_v4_signature/',
#     #      generate_aws_v4_signature,
#     #      name='s3direct-signing'),
# ]