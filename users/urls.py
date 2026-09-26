from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from users.views import CustomTokenObtainPairView, UserCreateAPIView


app_name = UsersConfig.name

urlpatterns = [
    path(
        "token/",
        CustomTokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=(AllowAny,)),
        name="token_refresh",
    ),
    path("register/", UserCreateAPIView.as_view(), name="register"),
]
