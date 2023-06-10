"""Ghibli URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 1111111111111111
from django.contrib import admin
from django.urls import include, path

# urlpatterns = [
#     path('api/', include('rest_framework.urls')),
#     path('', include('gbapp.urls')),
#     path('admin/', admin.site.urls),
# ]

# 2222222222222222
# from django.conf import settings  # new
# from django.conf.urls.static import static  # new
# from django.contrib import admin
# from django.urls import path, include
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('rest_framework.urls')), 
#     path('', include('gbapp.urls')), 
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# 3333333333333333333333

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')), 
    path('gbapp/', include('gbapp.urls')), 
]