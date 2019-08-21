from datetime import datetime

from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import render, redirect
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from newtest.forms import PostTweet, UserProfileInfoForm
from .serializers import TweetSerializer, UserProfileSerializer, \
    UserSerializer, FollowSerializer
from .models import UserProfile, Like
from .models import Follow
from .models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect

#remove unused imports


class CreateTweet(generics.CreateAPIView): #use ListCreateAPIView

    serializer_class = TweetSerializer
    permission_classes = (IsAuthenticated, )


class Logout(APIView):

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UserFollow(generics.ListCreateAPIView):
#missing queryset
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        user1 = self.request.query_params.get('username') #user1 to username
        user2=User.objects.get(username=user1) #user2 to user
        serializer.save(user=user2, followed_by=self.request.user)


class DisplayTweet(generics.ListAPIView): #not required
    serializer_class = TweetSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Tweet.objects.all()


class GetUserFollowing(generics.ListAPIView):
    #missing queryset
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        username = self.request.query_params.get("username")
        user_details= User.objects.get(username=username)
        follower_list = user_details.has_followers
        print(follower_list)
        queryset = follower_list
        return queryset


class DetailsViewTweet(generics.RetrieveUpdateDestroyAPIView):
    #TweetDetailView
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class CreateUser(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUserProfile(generics.CreateAPIView): #use ListCreateAPIView

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class DisplayUserProfile(generics.ListAPIView): #not required

    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)
    queryset = UserProfile.objects.all()


class DetailsUserProfile(generics.RetrieveUpdateDestroyAPIView): #UserProfileDetailView
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


