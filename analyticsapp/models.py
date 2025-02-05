from django.db import models
from app.models import Post
# Create your models here.

class TrackedPosts(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
