from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

from django import forms
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'gender', 'birth_date', 'growth', 'weight', 'activity', 'avatar', )


class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'gender', 'birth_date', 'growth', 'weight', 'activity', 'avatar',)


class CustomUserChangeFormAdmin(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'gender', 'birth_date', 'growth', 'weight', 'activity', 'avatar',)

