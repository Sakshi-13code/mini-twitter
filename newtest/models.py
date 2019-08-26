from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-created_on']

    def __str__(self):
        template = '{0.content} {0.user.username}'
        return template.format(self)

    @property
    def get_likes(self):
        return self.tweetlikes.count()


class FollowRelation(models.Model):

    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

    def clean(self):
        if self.following == self.follower:
            raise ValidationError({
                'Cannot Follow Yourself'
            })

    class Meta:
        unique_together = ("following", "follower")

    def __str__(self):
        template = '{0.following.username} {0.follower.username}'
        return template.format(self)
    #    return self.following.username, self.follower.username
    # add followed_by username


class TweetLike(models.Model):

    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='tweetlikes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userlike')

    class Meta:
        unique_together = ["tweet", "user"]
