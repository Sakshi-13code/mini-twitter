from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tweet, UserProfile, Follow, Likes


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('user','content')


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user','name','bio')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')


class TweetSerializer2(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class TweetSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'


class TweetSerializer4(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'
