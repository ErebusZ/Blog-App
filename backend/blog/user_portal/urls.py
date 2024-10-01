from django import urls
from rest_framework_simplejwt import views as jwt_views

from user_portal import views


urlpatterns = [
    urls.path("signup/", views.RegistrationView.as_view(), name="signup"),
    urls.path("login/", views.LoginView.as_view(), name="signup"),
    urls.path("refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    urls.path("validate_token/", views.ValidateTokenView.as_view(), name="token_refresh"),
]
