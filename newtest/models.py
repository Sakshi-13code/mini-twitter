
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.TextField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    id = models.IntegerField(primary_key=True)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.content


class Follow(models.Model):
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following', null=True)
    followers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers', null=True)

    def __str__(self):
        return self.following


class Likes(models.Model):
    tweet_id = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
