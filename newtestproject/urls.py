"""newtestproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView)

from newtest import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),




    #url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('Tweet/', views.DisplayTweet.as_view(), name='tweet'),

    path('Tweet/Create', views.CreateTweet.as_view(), name='create_tweet'),

    path('Tweet/<int:pk>', views.DetailsViewTweet.as_view(), name='details_tweet'),

    path('User/Create', views.CreateUser.as_view(), name='create_user'),

    path('Profile/Create', views.CreateUserProfile.as_view(), name='create_profile'),

    path('User/', views.DisplayUserProfile.as_view(), name = 'display_users'),

    path('User/<int:pk>', views.DetailsUserProfile.as_view(), name = 'details_users'),

#    path('Follow/', views.FollowView.as_view(), name='follow'),

 #   path('Like/', views.LikeView.as_view(), name='like'),

    path('home/', views.home, name='home'),

    path('login/', views.login_page, name='login'),

    path('signup/', views.signup, name='signup'),

    path('pagelogout/',views.pagelogout, name='pagelogout'),

    path('', views.first_page, name='firstpage'),

    path('incorrect/', views.incorrect,name='incorrect'),

    path('profile/', views.profile1, name='profile1'),

    path('<str:username>/profile/', views.profile, name='profile'),

    path('profile/new/', views.post_new, name='post_tweet'),

    path('unihome/',views.unihome, name='unihome')

    #   path('profile/<str:username>/',views.follower_details,name='follower_details')


]
