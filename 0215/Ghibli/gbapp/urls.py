from django.urls import path, include
from . import views
from .views import helloAPI, upload_image
                            # Image

urlpatterns = [
    # 연습 api : http://localhost:8000/gbapp/hello/
    path("hello/", helloAPI),
    # path("download/", downloadAPI),
    path("upload_image/", upload_image),
    # stackover~ 추가
    # path("upload_image/<int:pk>/", upload_image),
    # path('image', views.Image.as_view(), name='image'),
]


# urlpatterns = [
#     path('image', views.Image.as_view(), name='image'),
# ]
