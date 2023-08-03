from django.forms import ModelForm
from .models import *
from users.models import CustomUser
from django import forms
from datetime import datetime


class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'carbohydrate', 'fats', 'protein', 'calorie', 'quantity', 'category']


class AddUserFoodItem_breakfast(ModelForm):

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='breakfast')
        self.fields['add_date'].initial = datetime.now().date()

class AddUserFoodItem_lunch(ModelForm):

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='lunch')
        self.fields['add_date'].initial = datetime.now().date()
class AddUserFoodItem_dinner(ModelForm):

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='dinner')
        self.fields['add_date'].initial = datetime.now().date()
class AddUserFoodItem_snacks(ModelForm):

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='snacks')
        self.fields['add_date'].initial = datetime.now().date()
class ChooseDateForm(ModelForm):

    class Meta:
        model = ChooseDate
        fields = ['c_date']

