from django.db import models

# Create your models here.
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
class Post(models.Model):
    creator = models.ForeignKey('auth.User', related_name='post', on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now=True)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
    views = models.IntegerField(default=0)

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
