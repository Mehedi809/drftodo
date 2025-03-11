from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIVIew,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework import viewsets
from restframework.permissions import Allowonly
from django.http import JsonResponse
from .models import *
from .serializers import *
# Create your views here.
