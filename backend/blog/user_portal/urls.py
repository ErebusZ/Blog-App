from django.urls import path


from user_portal import views


urlpatterns = [
    path("", views.RegistrationView.as_view(), name="signup"),
]
