from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comments(models.Model):
    comment = models.CharField(max_length=30)

class Follow(models.Model):
    author = models.ForeignKey(User, related_name= 'author', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name= 'follower' ,on_delete=models.CASCADE)

class Posts(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comments = models.ManyToManyField(Comments)
    likes = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)