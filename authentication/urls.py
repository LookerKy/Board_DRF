from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import LoginView, CustomUserRegister, hello_world, RefreshTokenView

urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
    path('user/create/', CustomUserRegister.as_view(), name='create_user'),
    path('token/obtain/', LoginView.as_view(), name='token_create'),  # override sjwt stock token
    # path('token//', jwt_views.TokenRefreshView.as_view(), name='token_refresh'), # this token has problem
    path('token/refresh/', RefreshTokenView.as_view(), name='test_refresh')
]
