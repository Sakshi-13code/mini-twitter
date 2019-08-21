from django import forms
from .models import Tweet


class PostTweet(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ('content',)


class UserProfileInfoForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    name = forms.CharField(widget=forms.TextInput())
    bio = forms.CharField(widget=forms.TextInput())
