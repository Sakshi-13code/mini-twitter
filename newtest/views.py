from django.db import IntegrityError
from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TweetSerializer, UserProfileSerializer, \
    UserSerializer, FollowSerializer, LikeSerializer
from .models import UserProfile, FollowRelation, TweetLike
from .models import Tweet
from django.contrib.auth.models import User


class CreateDisplayTweet(generics.ListCreateAPIView):

    serializer_class = TweetSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Tweet.objects.all()

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user, content=self.request.data["content"])


class Timeline(generics.ListAPIView):
    serializer_class = TweetSerializer

    def get_queryset(self):
        tweet_set = []
        current_user = self.request.user
        current_following = FollowRelation.objects.filter(follower=current_user)
        for follower in current_following:
            users = User.objects.get(username=follower.following)
            tweet_set.extend(Tweet.objects.filter(user=users))
        queryset = tweet_set
        return queryset


class Logout(APIView):

    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class LikeDislikeTweet(generics.ListCreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        tweet_id = self.kwargs['pk']
        tweet_obj = Tweet.objects.get(id=tweet_id)
        print(tweet_obj)

        try:
            serializer.save(tweet=tweet_obj, user=self.request.user)

        except IntegrityError:
            TweetLike.objects.get(tweet=tweet_obj, user=self.request.user).delete()


class UserFollowUnfollow(generics.ListCreateAPIView):
    # missing queryset
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    queryset = FollowRelation.objects.all()

    def perform_create(self, serializer):
        userid = self.kwargs['pk']
        username = User.objects.get(id=userid)
        print(username)
        user = User.objects.get(username=username)

        try:
            if user != self.request.user:
                serializer.save(following=user, follower=self.request.user)
            else:
                raise serializers.ValidationError("You cannot follow yourself")
        except IntegrityError:

            FollowRelation.objects.get(following=user, follower=self.request.user).delete()


class GetUserFollowing(generics.ListCreateAPIView):

    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    queryset = FollowRelation.objects.all()

    def perform_create(self, serializer):
        userid = self.kwargs['pk']
        username = User.objects.get(id=userid)
        print(username)
        user = User.objects.get(username=username)

        try:
            if user != self.request.user:
                serializer.save(following=self.request.user, follower=user)
            else:
                raise serializers.ValidationError("You cannot follow yourself")
        except IntegrityError:

            FollowRelation.objects.get(following=self.request.user, follower=user).delete()

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.kwargs['pk']
        queryset = queryset.filter(following=user)
        # follower_list = FollowRelation.objects.filter(following=user)
        # queryset = follower_list
        # print(follower_list)
        return queryset


class GetUserFollowers(generics.ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    queryset = FollowRelation.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.kwargs['pk']
        queryset = queryset.filter(follower=user)
        # following_list = FollowRelation.objects.filter(follower=user)
        # queryset = following_list
        return queryset


class TweetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class GetUserTweet(generics.ListAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.kwargs['pk']
        queryset=queryset.filter(user=user)
        return queryset


class CreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        User.objects.create_user(username=self.request.data['username'], password=self.request.data['password'])


class CreateDisplayUserProfile(generics.ListCreateAPIView):

    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class DisplayUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
