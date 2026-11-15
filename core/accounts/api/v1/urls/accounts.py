from django.urls import path
from .. import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("test_email/", views.TestEmailSend.as_view(), name="test_email"),
    # Registration
    path(
        "registration/",
        views.RegistrationApiView.as_view(),
        name="registration",
    ),
    # activation
    path(
        "activation/confirm/<str:token>",
        views.ActivationAPIView.as_view(),
        name="activation",
    ),
    # activation
    path(
        "activation/resend/",
        views.ActivationResendAPIView.as_view(),
        name="activation-resend",
    ),
    # login token
    path(
        "token/login/",
        views.CustomObtainAuthToken.as_view(),
        name="token_login",
    ),
    path(
        "token/logout/",
        views.CustomDiscardAuthToken.as_view(),
        name="token_logout",
    ),
    # login jwt
    path(
        "jwt/login/",
        views.CustomTokenObtainPairView.as_view(),
        name="jwt_login",
    ),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt_verify"),
    # change password
    path(
        "change-password/",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    path(
        "reset-password/",
        views.ResetPasswordEmailApiView.as_view(),
        name="reset-password",
    ),
    path(
        "reset-password/confirm/<str:uidb64>/<str:token>/",
        views.ResetPasswordConfirmApiView.as_view(),
        name="reset-password-confirm",
    ),
]
