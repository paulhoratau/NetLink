from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from . import views

urlpatterns = [

    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', views.CreateUserView.as_view(), name='register'),
    path('search/users', views.SearchUsers.as_view(), name='search'),
    path('profile/', views.ProfileDetailed.as_view(), name="user_profile"),
]
