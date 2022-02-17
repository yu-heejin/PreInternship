from rest_framework.routers import SimpleRouter
from .views import *
from django.urls import path, re_path

'''
router = SimpleRouter()
router.register('s3anddb', DropBoxViewset)

urlpatterns = router.urls
'''

urlpatterns = [
    re_path(r'^jdb$', PostView.as_view(), name='file-test'),
    #  re_path(r'^serv/([0-9]+)$', File
    # TestViewSet.as_view()),
]
