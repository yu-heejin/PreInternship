from rest_framework.routers import SimpleRouter
from s3api import views
from .views import *
from django.urls import path, re_path

router = SimpleRouter()
router.register('accounts', DropBoxViewset)

urlpatterns = router.urls

