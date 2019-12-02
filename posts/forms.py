# Django
from django import forms

# Models
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:

        model = Post
        fields = ('user', 'profile', 'title', 'picture')    