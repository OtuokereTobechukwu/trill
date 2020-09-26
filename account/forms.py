from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms. CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['password2']
#
# class UserRegistrationForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'input',
#         'type': 'text',
#         'placeholder': 'Enter username'
#     }))
#
#     email = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'input',
#         'type': 'email',
#         'placeholder': 'Enter email address'
#     }))
#
#     password1 = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'input',
#         'type': 'password',
#         'placeholder': 'Enter password'
#     }))
#
#     password2 = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'input',
#         'type': 'password',
#         'placeholder': 'Confirm password'
#     }))
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
#
#     def clean_password2(self):
#         cd = self.cleaned_data
#         if cd['password'] != cd['password2']:
#             raise forms.ValidationError('Passwords don\'t match')
#         return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')