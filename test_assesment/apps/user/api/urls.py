from rest_framework import routers
from django.urls import path, include
from .views import RegisterView, LoginView, ForgotPasswordView, ResetPasswordView
from test_assesment.apps.user.api import views as user_views


router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('forget-password/', ForgotPasswordView.as_view(), name='forget-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
]