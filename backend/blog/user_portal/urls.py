from django.urls import path
#     TokenObtainPairView,
#     TokenRefreshView,
# )

from user_portal import views


urlpatterns = [
    path("signup/", views.RegistrationView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="signup"),
]
