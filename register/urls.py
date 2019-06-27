"""test2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from . import  views
from django.conf.urls import url
from django.views.generic import ListView, DetailView
from register.models import Articels
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
urlpatterns = [

    path('register/', views.register),
    path('login/', views.login),
    # path('', views.homepage),
    # path('base', views.base),

    path('', ListView.as_view(queryset=Articels.objects.all().order_by("-date")[:20],template_name='MainPage/index.html') ),
    url(r'^car/(?P<pk>\d+)/$',DetailView.as_view(model= Articels,template_name='MainPage/single-car.html')),
     url(r'^list/$', ListView.as_view(queryset=Articels.objects.all().order_by("-date")[:100],template_name='MainPage/list.html')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
