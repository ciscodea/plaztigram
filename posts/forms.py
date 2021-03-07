""" Post forms"""

from django import forms
from posts.models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'user', 'profile', 'title', 'photo'}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = {'user', 'profile', 'post', 'text'}