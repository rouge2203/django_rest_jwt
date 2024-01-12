from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .views import UserViewSet
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_users/", views.get_users, name="get_users"),

]