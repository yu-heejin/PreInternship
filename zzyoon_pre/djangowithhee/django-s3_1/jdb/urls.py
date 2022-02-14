from importlib.resources import read_binary
from winreg import REG_OPTION_OPEN_LINK
from django.urls import URLPattern
from jdb import views
from django.urls import path, re_path

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    re_path(r'^img$', views.ImgApi),
    re_path(r'^img/([0-9]+)$', views.ImgApi),

    # re_path(r'^img/savefile', views.savefile)
]

# +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
