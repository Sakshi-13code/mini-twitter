from django.conf.urls import url
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [

    path('token/', obtain_auth_token, name='token'), #change name to login
  #  url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('Tweet/', views.DisplayTweet.as_view(), name='tweet'), #LisctCreate in single view, same for Userprofile and user

    path('Tweet/Create', views.CreateTweet.as_view(), name='create_tweet'), #not required

    path('Logout/', views.Logout.as_view(), name='logout'),

    path('Tweet/<int:pk>', views.DetailsViewTweet.as_view(), name='details_tweet'),

    path('User/Create', views.CreateUser.as_view(), name='create_user'),

    path('Profile/Create', views.CreateUserProfile.as_view(), name='create_profile'),

    path('User/', views.DisplayUserProfile.as_view(), name='display_users'),

    path('User/<int:pk>', views.DetailsUserProfile.as_view(), name='details_users'),

    path('Following/', views.GetUserFollowing.as_view(), name='display_followers'),

    path('Follow/',views.UserFollow.as_view(), name='follow_users')




]
#users/ (GET, POST)
'''users/<user_id> (GET, PUT, DELETE)
user_id/followers/
user_id/following/
tweets/ (GET, POST)
tweets/<tweet_id> (GET, PUT, DELETE)
user_id/tweets/
tweet_id/like'''

'''
    like and unlike a tweet
    unfollow
    timeline
    edit bio in a profile and edit contents of a tweet
'''

