from django.urls import path, include

from .views import (
    SignupAPI,
    LoginAPI,
    ProfileAPI,
    ProfileUpdateAPI,
    ProfileListAPI,
    PasswordAPIView
)


urlpatterns = [
    path('', ProfileListAPI.as_view(), name='profile_list_api'),
    path('register/', SignupAPI.as_view(), name='singup_api'),
    path('login/', LoginAPI.as_view(), name='login_api'),
    path('<str:username>/', ProfileAPI.as_view(), name='profile_api'),
    path('<str:username>/profile/', ProfileUpdateAPI.as_view(), name='profile_update_api'),
    path('<str:username>/password/', PasswordAPIView.as_view(), name='password_api'),
]
