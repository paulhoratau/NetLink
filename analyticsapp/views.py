from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post

class TrackPostView(APIView):
    def post(self, request, post_id):
        post = get_object_or_404(Post, pk=post_id)
        post.count += 1
        post.save()

        return Response({'message': 'Post tracked', 'views': post.count})
