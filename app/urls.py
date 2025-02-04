from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', views.CreateUserView.as_view(), name='register'),
    path('search/users', views.SearchUsers.as_view(), name='search'),
    path('profile/', views.ProfileDetailed.as_view(), name="user_profile"),
    path('post/', views.PostCreate.as_view(), name="post"),
    path('post/<int:pk>', views.PostDetailed.as_view(), name="post-detailed"),
    path('comment/', views.CommentList.as_view(), name='comment-list-create'),
    path('comment/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),
    path('comment/<int:pk>/replies/', views.CommentReply.as_view(), name='comment-reply'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
