from rest_framework import permissions, generics
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import UserSearchSerializer, UserSerializer, UserProfileSerializer, PostSerializer, CommentSerializer, CommentReplySerializer
from .models import Post, Comment, CommentReply
from rest_framework.parsers import MultiPartParser, FormParser

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



class PostCreate(CreateAPIView):
    queryset = Post.objects.order_by('-creation_date')
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class PostDetailed(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentReply(generics.ListCreateAPIView):
    queryset = CommentReply.objects.all()
    serializer_class = CommentReplySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
