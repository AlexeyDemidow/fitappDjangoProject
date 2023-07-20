from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group
from .finder import FoodItemFilter
from users.models import CustomUser
from datetime import datetime, date, time
from django.http import HttpResponse
from .models import FoodItem, UserFoodItem

from .forms import FoodItemForm



# Create your views here.

@login_required
def calc_main(request):
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()[:5]
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()[:5]
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()[:5]
    snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()[:5]
    customers = CustomUser.objects.all()
    context = {'breakfast': breakfast,
               'lunch': lunch,
               'dinner': dinner,
               'snacks': snacks,
               'customers': customers,
               }
    return render(request, 'calc_main.html', context)


def fooditem(request):
    breakfast = Category.objects.filter(name='breakfast')[0].fooditem_set.all()
    bcnt = breakfast.count()
    lunch = Category.objects.filter(name='lunch')[0].fooditem_set.all()
    lcnt = lunch.count()
    dinner = Category.objects.filter(name='dinner')[0].fooditem_set.all()
    dcnt = dinner.count()
    snacks = Category.objects.filter(name='snacks')[0].fooditem_set.all()
    scnt = snacks.count()
    context = {'breakfast': breakfast,
               'bcnt': bcnt,
               'lcnt': lcnt,
               'scnt': scnt,
               'dcnt': dcnt,
               'lunch': lunch,
               'dinner': dinner,
               'snacks': snacks,
               }
    return render(request, 'fooditem.html', context)


@login_required
def createfooditem(request):
    form = FoodItemForm()
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/calories_calc/user_calc/')
    context = {'form': form}
    return render(request, 'createfooditem.html', context)


def user_calc(request):
    user = request.user
    cust = user.id
    fooditems = FoodItem.objects.filter()
    myfilter = FoodItemFilter(request.GET, queryset=fooditems)
    fooditems = myfilter.qs
    total = UserFoodItem.objects.all()
    myfooditems = total.filter(customer=cust)
    cnt = myfooditems.count()
    querysetFood = []
    for food in myfooditems:
        querysetFood.append(food.fooditem.all())
    finalFoodItems = []
    for items in querysetFood:
        for food_items in items:
            finalFoodItems.append(food_items)
    totalCalories = 0
    dailyCalories = user.calories_per_day()
    for foods in finalFoodItems:
        totalCalories += foods.calorie
    '''if datetime.strftime(datetime.now(), "%H:%M") == datetime.strptime('14:14', "%H:%M"):
        finalFoodItems.clear()'''
    CalorieLeft = dailyCalories - totalCalories

    context = {'CalorieLeft': CalorieLeft, 'totalCalories': totalCalories, 'cnt': cnt, 'foodlist': finalFoodItems,
               'fooditem': fooditems, 'myfilter': myfilter}
    return render(request, 'user_calc.html', context)

@login_required
def addFooditem(request):
    user = request.user
    if request.method == "POST":
        form = AddUserFoodItem(request.POST, initial={'customer':  user})
        if form.is_valid():
            form.save()
            return redirect('/calories_calc/user_calc/')
    form = AddUserFoodItem(initial={'customer':  user})
    context = {'form': form}
    return render(request, 'AddUserFoodItem.html', context)

@login_required
def deleteFooditem(request):
    user = request.user
    cust = user.id
    total = UserFoodItem.objects.all()

    myfooditems = total.filter(customer=cust)

    reverse_myfooditems = myfooditems[::-1]
    reverse_myfooditems[0].delete()

    return redirect('/calories_calc/user_calc/')

