# lotto/urls.py

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from django.conf import settings
from board import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('board.urls')),

]