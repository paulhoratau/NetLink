from django.db import models

# Create your models here.
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)
class Post(models.Model):
    creator = models.ForeignKey('auth.User', related_name='post', on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now=True)
    image_url = models.ImageField(upload_to=upload_to, blank=True, null=True)
