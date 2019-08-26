
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [

    path('login', obtain_auth_token, name='token'),

    path('logout', views.Logout.as_view(), name='logout'),

    path('signup', views.CreateUser.as_view(), name='create_user'),

    path('users', views.CreateDisplayUserProfile.as_view(), name='create_profile'),

    path('users/<int:pk>', views.UserProfileDetailView.as_view(), name='details_users'),

    path('users/<int:pk>/tweets', views.GetUserTweet.as_view(), name='tweets'),

    path('users/<int:pk>/followers', views.GetUserFollowing.as_view(), name='display_followers'),

    path('users/<int:pk>/following', views.GetUserFollowers.as_view(), name='display_followers'),

    path('tweets', views.CreateDisplayTweet.as_view(), name='tweet'),

    path('tweets/<int:pk>', views.TweetDetailView.as_view(), name='details_tweet'),

    path('tweets/<int:pk>/like', views.LikeDislikeTweet.as_view(), name='like'),

    path('timeline/', views.Timeline.as_view(), name='timeline'),

    path('follow/<int:pk>', views.UserFollowUnfollow.as_view(), name='follow_users'),

    # path('unfollow/<int:pk>', views.Unfollow.as_view(),name='unfollow')

]
# users/ (GET, POST)
'''users/<user_id> (GET, PUT, DELETE)
user_id/followers/
user_id/following/
tweets/ (GET, POST)  #done
tweets/<tweet_id> (GET, PUT, DELETE)
user_id/tweets/
tweet_id/like'''

'''
    like and unlike a tweet    #done
    unfollow #done
    timeline #done
    edit bio in a profile and #done
    edit contents of a tweet #done
'''
