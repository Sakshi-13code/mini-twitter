from django.contrib import admin

# Register your models here.


from newtest.models import FollowRelation, TweetLike, UserProfile, Tweet

admin.site.register(FollowRelation)
admin.site.register(TweetLike)
admin.site.register(UserProfile)
admin.site.register(Tweet)
