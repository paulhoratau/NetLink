from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User as UserModel
from .models import Post, Comment, CommentReply

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email'),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
        )
        user.save()
        return user

    class Meta:
        model = UserModel
        fields = ("id", "username", "password", "email", "first_name", "last_name")


class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', "first_name", "last_name"]

class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='username.username')
    class Meta:
        model = UserModel
        fields = ['id', 'username', 'email', "first_name", "last_name"]

class CommentReplySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comment = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all())

    class Meta:
        model = CommentReply
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    replies = CommentReplySerializer(many=True, read_only=True, source="commentreply")

    class Meta:
        model = Comment
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')
    creator_id = serializers.ReadOnlyField(source='creator.id')
    image_url = serializers.ImageField(required=False)
    content = serializers.CharField(max_length=255)
    creation_date = serializers.DateField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
