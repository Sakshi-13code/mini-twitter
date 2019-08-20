from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import render, redirect
from rest_framework import generics, permissions
from .serializers import TweetSerializer, TweetSerializer2, TweetSerializer3, TweetSerializer4, UserProfileSerializer, \
    UserSerializer
from .models import UserProfile, Likes
from .models import Follow
from .models import Tweet
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect


class DisplayTweet(generics.ListAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (permissions.IsAuthenticated,)


class CreateTweet(generics.CreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class DetailsViewTweet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUserProfile(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class DisplayUserProfile(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class DetailsUserProfile(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


def home(request):
    user1 = request.user.username
    button_text = " "
    flag_list = []
    i=0
    final_list = []

    following_list = Follow.objects.filter(following__username=user1)
    following1 = []
    for item in following_list:
        following1.append(item.followers.username)
    tweets = Tweet.objects.filter(user__username__in=following1)
    '''for t in tweets:
        flag_list.append(like_tweet(request,t))

    for t in tweets:
        final_list.append([t,flag_list[i]])
        i=i+1
    print(final_list)'''
    if request.method == 'POST':
        tweetid = request.POST.get('tweetid', '')
        if Likes.objects.filter(tweet_id__id=tweetid, user_id__username=user1):
            Likes.objects.filter(tweet_id__id=tweetid, user_id=request.user).delete()
            like_count = Tweet.objects.get(id=tweetid).like
            Tweet.objects.filter(id=tweetid).update(like=like_count-1)


        else:
            Likes(tweet_id=Tweet.objects.get(id=tweetid), user_id=request.user).save()
            like_count = Tweet.objects.get(id=tweetid).like
            Tweet.objects.filter(id=tweetid).update(like=like_count + 1)

    for t in tweets:
        flag_list.append(like_tweet(request,t))

    for t in tweets:
        final_list.append([t,flag_list[i]])
        i=i+1
    print(final_list)

    for element in final_list:
        print(element[1])


    return render(request, 'mytwitter/home.html', {'tweets': tweets,'final':final_list})


def post_new(request):
    if request.method == "POST":
        form = PostTweet(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user

            post.save()
            return redirect('mytwitter:profile1')
    else:
        form = PostTweet()
    return render(request, 'mytwitter/post_tweet.html', {'form': form})


def first_page(request):
    return render(request, 'mytwitter/first_page.html')


def signup(request):
    form = UserProfileInfoForm(request.POST or None)
    if request.method == 'POST':
        data = request.POST
        usrnme = data['username']
        pass1 = data['password1']
        pass2 = data['password2']
        nme = data['name']
        bi = data['bio']

        if pass1 == pass2:
            usr = User.objects.create_user(username=usrnme, password=pass1)
            UserProfile(user=usr, name=nme, bio=bi).save()

        return redirect('mytwitter:login')

    return render(request, 'mytwitter/signup.html', {'form': form})


def pagelogout(request):
    return render(request,'mytwitter/first_page.html')


def unihome(request):
    tweet = Tweet.objects.all()
    flag_list = []
    final_list = []
    i=0
    #for t in tweet:
    #    flag_list.append(like_tweet(request,t))
    #print(flag_list)
    if request.method == 'POST' and request.POST.get('tweetid', ''):
        tweetid = request.POST.get('tweetid', '')
        if Likes.objects.filter(tweet_id__id=tweetid, user_id__username=request.user):
            Likes.objects.filter(tweet_id__id=tweetid, user_id=request.user).delete()
            like_count = Tweet.objects.get(id=tweetid).like
            Tweet.objects.filter(id=tweetid).update(like=like_count-1)

        else:
            Likes(tweet_id=Tweet.objects.get(id=tweetid), user_id=request.user).save()
            like_count = Tweet.objects.get(id=tweetid).like
            Tweet.objects.filter(id=tweetid).update(like=like_count + 1)
    #current_following = Follow.objects.filter(following__username = request.user)

    for t in tweet:
        flag_list.append(like_tweet(request,t))

    for t in tweet:
        final_list.append([t,flag_list[i]])
        i=i+1

    print(final_list)








    return render(request,'mytwitter/uni.html', {'tweet':tweet,'final':final_list})


def like_tweet(request,tweet):
    info = UserProfile.objects.get(user=request.user)
    res = Likes.objects.filter(tweet_id = tweet.id, user_id =info.user)
    if res:
        return 1
    else:
        return 0


def profile(request, username):
    user1 = username
    u = User.objects.get(username=user1)

    ur = request.user
    button_text= ""
    if Follow.objects.filter(following=ur, followers=u):
        button_text="unfollow"
    else:
        button_text="follow"

    if request.method == 'POST' and request.POST.get('follow', ''):

        if Follow.objects.filter(following=ur, followers=u):
            Follow.objects.filter(following=ur, followers=u).delete()
            button_text="follow"
        else:
            Follow(following=ur, followers=u).save()
            button_text="unfollow"

    follower_list = Follow.objects.filter(followers__username=user1)

    name = UserProfile.objects.filter(user__username=user1)
    tweet = Tweet.objects.filter(user__username=user1)
    bio1 = UserProfile.objects.get(user__username=user1)
    bio2 = bio1.bio
    following2 = []
    for item in follower_list:
        following2.append(item.following.username)
    following_list1 = Follow.objects.filter(following__username=user1)

    following1 = []

    for item in following_list1:
        following1.append(item.followers.username)
    return render(request, 'mytwitter/profile.html', {'followers': following2, 'following': following1, 'name': name,
                                                      'tweet': tweet, 'username': user1, 'bio': bio2,'button':button_text})




def profile1(request):
    #   user1 = username
    user1 = request.user.username
    if request.method == 'POST' and request.POST.get('follow', ''):
        fid = request.POST.get('follow', '')
        print(fid)
        u = User.objects.get(username=fid)
        ur = User.objects.get(username=request.user.username)
        print(ur)
        Follow.objects.create(following=ur, followers=u)
        print('hey')

    follower_list = Follow.objects.filter(followers__username=user1)
    name = UserProfile.objects.filter(user__username=user1)
    tweet = Tweet.objects.filter(user__username=user1)
    bio1 = UserProfile.objects.get(user__username=user1)
    bio2 = bio1.bio

    following2 = []
    for item in follower_list:
        following2.append(item.following.username)
    following_list1 = Follow.objects.filter(following__username=user1)

    following1 = []

    for item in following_list1:
        following1.append(item.followers.username)

    if request.method == 'POST' and request.POST.get('follow', ''):
        fid = request.POST.get('follow','')
        print(fid)
        u=User.objects.get(username=fid)
        ur = User.objects.get(username=request.user.username)
        print(ur)
        Follow.objects.create(following=ur, followers=u )
        print('hey')

    return render(request, 'mytwitter/profile.html',
                  {'followers': following2, 'following': following1, 'name': name, 'tweet': tweet, 'username': user1,
                   'bio': bio2})


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username", '')
        password = request.POST.get("password", '')
        user = authenticate(request, username=username, password=password)
        #print(username, password)

        # user = User.objects.create(username=username, password=password)
        print(user)
        if user is not None:
            django_login(request, user)
            #print('hey im inside')
            return redirect('mytwitter:profile1')
        else:
            return redirect('mytwitter:incorrect')
    # else:
    #    return render(request, 'mytwitter/login.html')
    return render(request, 'mytwitter/login.html')

def incorrect(request):
    return render(request,'mytwitter/incorrect.html')

def follower_details(name):
    user1 = name
    follower_list = Follow.objects.filter(followers__username=user1)
    following2 = []

    for item in follower_list:
        following2.append(item.following.username)
    following_list1 = Follow.objects.filter(following__username=user1)

    following1 = []

    for item in following_list1:
        following1.append(item.followers.username)

    return render('mytwitter/details.html', {'followers': following2, 'following': following1, 'name': user1})
