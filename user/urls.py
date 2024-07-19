from django.urls import path, include
from .views import *

app_name = "user"

urlpatterns = [
    path("", homeView, name="home"),
    path("signup/", signupView, name="sign-up"),
    path("login/", loginView, name="login"),
    path("logout/", logoutView, name="logout"),
]
