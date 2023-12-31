from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *
from django.forms import ModelForm
from datetime import datetime


class CustomUserCreationForm(UserCreationForm):
    """Форма создания пользователя"""

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'gender', 'birth_date', 'growth', 'weight', 'activity', 'avatar', 'calories']


class CustomUserChangeForm(UserChangeForm):
    """Форма изменения данных пользователя"""

    password = None

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'gender', 'birth_date', 'growth', 'activity', 'avatar', 'calories']


class CustomUserChangeFormAdmin(UserChangeForm):
    """Форма изменения данных пользователя в админ-панели"""

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'gender', 'birth_date', 'growth', 'weight', 'activity', 'avatar', 'calories']


class WeighingForm(ModelForm):
    """Форма взвешивания"""

    class Meta:
        model = Weighing
        fields = ['user', 'weight_value', 'weighing_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = CustomUser.objects.filter(username=self.initial['user'])
        self.fields['weighing_date'].initial = datetime.now()
