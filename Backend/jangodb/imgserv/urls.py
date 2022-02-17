from django.urls import re_path
from .views import FileTestViewSet

urlpatterns = [
    re_path(r'^serv$', FileTestViewSet.as_view(), name='file-test'),
    #  re_path(r'^serv/([0-9]+)$', FileTestViewSet.as_view()),
]

'''
urlpatterns = [
    re_path(r'^serv$', ImgSevApi),
    re_path(r'^serv/([0-9]+)$', ImgSevApi),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
