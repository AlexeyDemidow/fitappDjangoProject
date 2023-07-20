from django.forms import ModelForm
from .models import *
from users.models import CustomUser
from django import forms



class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'carbohydrate', 'fats', 'protein', 'calorie', 'quantity']


class AddUserFoodItem(ModelForm):
    #customer = forms.ModelChoiceField(queryset=CustomUser.objects.all(), widget=forms.HiddenInput())
    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])

