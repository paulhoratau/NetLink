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

    path('profile/<int:pk>/', views.ProfileDetailed.as_view(), name="user_profile"),

    path('post/', views.PostCreate.as_view(), name="post"),
    path('post/<int:pk>', views.PostDetailed.as_view(), name="post-detailed"),
    path('post/<int:pk>/manage/', views.PostManage.as_view(), name="post-manage"),
    path('post/<int:pk>/manage/delete/', views.PostDelete.as_view(), name="post-delete"),
    path('post/<int:post_id>/comments/', views.CommentsAPIView.as_view({'get': 'list'}), name='all_comments'),

    path('comment/', views.CommentList.as_view(), name='comment-list-create'),
    path('comment/<int:pk>/', views.CommentDetail.as_view(), name='comment-detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
