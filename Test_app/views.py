from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from .models import *
from .serializers import *
# Create your views here.

class UserListAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


class UserCreateAPIView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers