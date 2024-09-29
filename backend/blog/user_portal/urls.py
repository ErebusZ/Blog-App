from django import urls

from user_portal import views


urlpatterns = [
    urls.path("signup/", views.RegistrationView.as_view(), name="signup"),
    urls.path("login/", views.LoginView.as_view(), name="signup"),
]
