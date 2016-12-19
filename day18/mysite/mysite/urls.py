"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app01 import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^index/', views.f1),
    # url(r'^login/', views.login),
    # url(r'^deteil/(\d+)/', views.deteil),
    # url(r'^deteil1/(\d+)/(\d+)/', views.deteil1),
    # url(r'^deteil2/(?P<p1>\d+)/(?P<x2>\d+)/', views.deteil2),
    # url(r'^index/(\d+)/', views.index),
    # url(r'^detail/(\d+)/', views.detail),
    url(r'^web/', include('app01.urls'))

]
