from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import LoginView, CustomUserRegister, user_profile, RefreshTokenView, UserRegisterView, user_register

urlpatterns = [
    path('me/', user_profile, name='profile_user'),
    path('user/create/', user_register, name='create_user'),
    path('token/obtain/', LoginView.as_view(), name='token_create'),  # override sjwt stock token
    # path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('refresh/token/', RefreshTokenView.as_view(), name='test_refresh')
]
