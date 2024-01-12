from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import UserSerializer
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Api View")

from rest_framework.views import APIView
from rest_framework.response import Response

def get_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, safe=False)
    else:
        return Response("Invalid Request")
    
