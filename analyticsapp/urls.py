
from django.urls import path
from . import views

urlpatterns = [
    path('postcount/<int:post_id>', views.TrackPostView.as_view(), name="TrackPostView"),
]
