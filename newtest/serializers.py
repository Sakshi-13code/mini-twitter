from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tweet, UserProfile, Follow, Like


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('id', 'user', 'get_username', 'content', 'get_likes')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user', 'name', 'bio') #userid instead of user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('user', 'followed_by') #user_id and followed_by_id


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('tweet', 'user') #tweet_id and user_id

