from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tweet, UserProfile, FollowRelation, TweetLike


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('id', 'user', 'content', 'get_likes')
        read_only_fields = ('id', 'user', 'get_likes')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user_id', 'name', 'bio')
        # userid instead of user
        read_only_fields = ('user_id', 'name')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowRelation
        fields = ('following_id', 'follower_id')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetLike
        fields = ('tweet_id', 'user_id')

