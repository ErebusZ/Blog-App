from django.contrib import admin
from django import urls


urlpatterns = [
    urls.path("admin/", admin.site.urls),
    urls.path("user_portal/", urls.include("user_portal.urls")),
    urls.path("articles/", urls.include("articles.urls")),
]
