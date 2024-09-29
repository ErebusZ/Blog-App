from django.db import models
from django.contrib.auth import models as django_models


class BlogPost(models.Model):
    author = models.ForeignKey(
        django_models.User, on_delete=models.CASCADE, related_name="publications"
    )
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="blog_images", blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
