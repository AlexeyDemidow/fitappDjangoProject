from django.forms import ModelForm
from .models import *
from users.models import CustomUser
from datetime import datetime
import django_filters
from django import forms


class FoodItemForm(ModelForm):
    class Meta:
        model = FoodItem
        fields = ['name', 'calorie', 'protein', 'fats', 'carbohydrate', 'quantity']


class AddUserFoodItem_breakfast(ModelForm):

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='breakfast')
        self.fields['add_date'].initial = datetime.now().date()


class AddUserFoodItem_lunch(ModelForm):

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='lunch')
        self.fields['add_date'].initial = datetime.now().date()


class AddUserFoodItem_dinner(ModelForm):

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='dinner')
        self.fields['add_date'].initial = datetime.now().date()


class AddUserFoodItem_snacks(ModelForm):

    class Meta:
        model = UserFoodItem
        fields = ['customer', 'fooditem', 'category', 'add_date', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['category'].initial = Category.objects.get(name='snacks')
        self.fields['add_date'].initial = datetime.now().date()


class ChooseDateForm(ModelForm):

    class Meta:
        model = ChooseDate
        fields = ['c_date']


class WaterTrackerForm(ModelForm):

    class Meta:
        model = WaterTracker
        fields = ['glass', 'drink_date', 'customer']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = CustomUser.objects.filter(username=self.initial['customer'])
        self.fields['drink_date'].initial = datetime.now().date()


class CSVupload(forms.Form):
    csv_file = forms.FileField()