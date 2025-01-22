from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model  # If using a custom user model

from .serializers import UserSerializer

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]  # Allow any user to access this view
    serializer_class = UserSerializer
