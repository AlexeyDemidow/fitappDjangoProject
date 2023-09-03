from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.forms import ModelForm
from datetime import datetime


# Форма создания пользователя
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'gender', 'birth_date', 'growth', 'weight', 'activity', 'avatar', 'calories']


# Форма изменения данных пользователя
class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'gender', 'birth_date', 'growth', 'activity', 'avatar', 'calories']


# Форма изменения данных пользователя в админпанели
class CustomUserChangeFormAdmin(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'gender', 'birth_date', 'growth', 'weight', 'activity', 'avatar', 'calories']


# Форма взвешивания
class WeighingForm(ModelForm):

    class Meta:
        model = Weighing
        fields = ['user', 'weight_value', 'weighing_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = CustomUser.objects.filter(username=self.initial['user'])
        self.fields['weighing_date'].initial = datetime.now()
