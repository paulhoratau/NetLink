from django.shortcuts import render
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import generics
from .serializers import UserSearchSerializer, UserSerializer, UserProfileSerializer
UserModel = get_user_model()

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

class SearchUsers(generics.ListAPIView):
    serializer_class = UserSearchSerializer
    def get_queryset(self):
        user = self.request.GET.get("username")
        if user:
            queryset = UserModel.objects.filter(username__icontains=user)
            print(type(queryset))
            return queryset
        else:
            return UserModel.objects.none()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return HttpResponse({"Doesn't exists"})
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ProfileDetailed(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user
