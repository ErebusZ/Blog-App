from rest_framework import permissions
from rest_framework import status
from rest_framework import response
from rest_framework import views
from rest_framework import exceptions
from rest_framework_simplejwt import authentication as jwt_auth
from django.db.models import Q
from django.core import paginator
from django.shortcuts import get_object_or_404


from articles import models
from articles import serializers


DEFAULT_PAGINATION = 10
DEFAULT_PAGE = 1


class BlogPostView(views.APIView):
    authentication_classes = [jwt_auth.JWTAuthentication]

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def get(self, request, blog_id=None):
        if blog_id is not None:
            blog_post = get_object_or_404(models.BlogPost, id=blog_id)
            serializer = serializers.BlogPostSerializer(blog_post)
            return response.Response(
                {"data": serializer.data, "message": "Success."},
                status=status.HTTP_200_OK,
            )

        articles = models.BlogPost.objects.all()
        if request.GET.get("search") is not None:
            keyword = request.GET.get("search")
            articles = articles.filter(
                Q(title__icontains=keyword) | Q(content__icontains=keyword)
            )
        page = request.GET.get("page", DEFAULT_PAGE)
        paginator_obj = paginator.Paginator(articles, DEFAULT_PAGINATION)
        try:
            page_content = paginator_obj.page(page)
        except paginator.EmptyPage:
            page_content = paginator_obj.page(paginator_obj.num_pages)
        except paginator.PageNotAnInteger:
            return response.Response(
                {"message": "Invalid page."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = serializers.BlogPostSerializer(page_content, many=True)
        return response.Response(
            {"data": serializer.data, "message": "Success."},
            status=status.HTTP_200_OK,
        )

    def post(self, request):
        try:
            data = request.data.copy()
            data["author"] = request.user.id
            serializer = serializers.BlogPostSerializer(data=data)

            if serializer.is_valid() is False:
                return response.Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()

            return response.Response(
                {"data": serializer.data, "message": "Success."},
                status=status.HTTP_201_CREATED,
            )

        except exceptions.ValidationError as e:
            return response.Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            data = request.data.copy()
            article_id = data.get("id")
            article = models.BlogPost.objects.filter(id=article_id)
            if article.exists() is False:
                return response.Response(
                    {"message": "Article not found."}, status=status.HTTP_404_NOT_FOUND
                )

            if article.filter(author=request.user).exists() is False:
                return response.Response(
                    {"message": "Unauthorized Action."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            serializer = serializers.BlogPostSerializer(
                article.last(), data=data, partial=True
            )

            if serializer.is_valid() is False:
                return response.Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()

            return response.Response(
                {"data": serializer.data, "message": "Success."},
                status=status.HTTP_201_CREATED,
            )
        except exceptions.ValidationError as e:
            return response.Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            data = request.data.copy()
            article_id = data.get("id")
            article = models.BlogPost.objects.filter(id=article_id)
            if article.exists() is False:
                return response.Response(
                    {"message": "Article not found."}, status=status.HTTP_404_NOT_FOUND
                )

            if article.filter(author=request.user).exists() is False:
                return response.Response(
                    {"message": "Unauthorized Action."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            article.delete()

            return response.Response(
                {"message": "Success."},
                status=status.HTTP_200_OK,
            )
        except exceptions.ValidationError as e:
            return response.Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
