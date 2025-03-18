from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/Userlistapiview/', UserListAPIView.as_view()),
    path('home/UserCreateapiview/', UserCreateAPIView.as_view()),
    path('home/UserUpdateAPIView/<int:id>/', UserUpdateAPIView.as_view()),

]
