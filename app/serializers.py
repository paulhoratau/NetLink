from rest_framework import serializers
from django.contrib.auth import get_user_model  # If using a custom user model

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ensure password is write-only

    def create(self, validated_data):
        # Create user with hashed password
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = UserModel
        fields = ("id", "username", "password", )  # Fields to be serialized

