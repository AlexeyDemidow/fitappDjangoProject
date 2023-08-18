from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'gender', 'birth_date', 'growth', 'weight', 'activity', 'avatar', 'calories',)


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'gender', 'birth_date', 'growth', 'weight', 'activity', 'avatar', 'calories',)


class CustomUserChangeFormAdmin(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'gender', 'birth_date', 'growth', 'weight', 'activity', 'avatar', 'calories',)
