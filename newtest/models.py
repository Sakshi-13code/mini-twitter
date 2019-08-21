
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')  #  related name not required
    bio = models.TextField()  # charfield
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #add related name
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True) #created at/on

    class Meta:

        ordering = ['-date']

    def __str__(self):
        return self.content
    #add user

    @property #not needed
    def get_username(self):
        return self.user.username

    @property #remove .all()
    def get_likes(self):
        return self.tweetlike.all().count()


class Follow(models.Model):
    #change model name
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='has_followers', null=True) #change related name
    followed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='is_followings', null=True) #remove null=true
    #change followed_by name
    def clean(self):
        if self.user == self.followed_by:
            raise ValidationError({
                'Cannot Follow Yourself'
            })

    class Meta:
        unique_together = ("user","followed_by")

    def __str__(self):
        return self.user.username
    #add followed_by username



class Like(models.Model):
    #change model name to tweetlike
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='tweetlike') #plural related name
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userlike')

    class Meta:
        unique_together = ["tweet", "user"]
