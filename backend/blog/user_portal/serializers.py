from rest_framework import serializers
from django.contrib.auth import models


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ["first_name", "last_name", "url", "username", "password", "email"]

    def validate(self, data):
        # if models.User.objects.filter(username=data["username"]).exists() is True:
        #     raise serializers.ValidationError("Username already taken.")
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
