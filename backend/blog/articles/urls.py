from django.urls import path

from articles import views


urlpatterns = [
    path("blog/", views.BlogPostView.as_view(), name="blog"),
    path("blog/<int:blog_id>/", views.BlogPostView.as_view(), name="blog"),
]
