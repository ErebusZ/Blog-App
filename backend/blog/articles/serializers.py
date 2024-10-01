from rest_framework import serializers
from .models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'image', 'content', 'created_at', 'updated_at', 'author']
        read_only_fields = ['created_at', 'updated_at']
