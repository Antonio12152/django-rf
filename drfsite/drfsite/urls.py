"""drfsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from blog.views import PostAPIList, PostAPIUpdate, PostAPIDelete, CatViewSet
from rest_framework import routers

routerCat = routers.SimpleRouter()
routerCat.register(r'cats', CatViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/postlists/', PostAPIList.as_view()),
    path('api/v1/postlists/<int:pk>/', PostAPIUpdate.as_view()),
    path('api/v1/postdelete/<int:pk>/', PostAPIDelete.as_view()),
    path('api/v1/', include(routerCat.urls)),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/',include('djoser.urls.authtoken'))
]