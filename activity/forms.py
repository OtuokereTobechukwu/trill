from django import forms
from .models import Posts
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify

class PostCreateForm(forms.ModelForm):

    def save(self, force_insert=False, force_update=False, commit=True):
        posts = super().save(commit=False)
        name = slugify(posts.title)
        if commit:
            posts.save()
        return posts

    class Meta:
        model = Posts
        fields = ('image', 'description')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('image', 'description')