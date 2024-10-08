from rest_framework import serializers
from django.contrib.auth import models
from django.contrib import auth
from rest_framework_simplejwt import tokens


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["first_name", "last_name", "url", "username", "password", "email"]

    def validate(self, data):
        required_fields = ["username", "email", "password", "first_name", "last_name"]
        for field in required_fields:
            if field not in data:
                raise serializers.ValidationError(f"{field} is required.")

        if models.User.objects.filter(username=data["username"]).exists() is True:
            raise serializers.ValidationError("Username already taken.")
        return data

    def create(self, validated_data):
        user = models.User.objects.create_user(
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        required_fields = ["username", "password"]
        for field in required_fields:
            if field not in data:
                raise serializers.ValidationError(f"{field} is required.")

        if models.User.objects.filter(username=data["username"]).exists() is False:
            raise serializers.ValidationError("Invalid username or password.")

        return data

    def get_token(self, data):
        user = auth.authenticate(username=data["username"], password=data["password"])

        if user is None:
            raise serializers.ValidationError("Invalid username or password.")

        refresh = tokens.RefreshToken.for_user(user)
        return {
            "message": "Success.",
            "data": {
                "userId": user.id,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
        }
