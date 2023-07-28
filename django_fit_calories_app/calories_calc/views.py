from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import FoodItem, UserFoodItem
from .forms import FoodItemForm
from datetime import date

# Create your views here.

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



    breakfast = Category.objects.filter(name='breakfast')[0].userfooditem_set.all()
    my_breakfast = breakfast.filter(customer=cust)
    bcnt = my_breakfast.count()
    breakfast_list = []
    for item in my_breakfast:
        breakfast_list.append(item.fooditem.all())
    breakfast_view_list = []
    for items in breakfast_list:
        for br_food in items:
            breakfast_view_list.append(br_food)


    lunch = Category.objects.filter(name='lunch')[0].userfooditem_set.all()
    my_lunch = lunch.filter(customer=cust)
    lcnt = my_lunch.count()
    lunch_list = []
    for item in my_lunch:
        lunch_list.append(item.fooditem.all())
    lunch_view_list = []
    for items in lunch_list:
        for lc_food in items:
            lunch_view_list.append(lc_food)

    dinner = Category.objects.filter(name='dinner')[0].userfooditem_set.all()
    my_dinner = dinner.filter(customer=cust)
    dcnt = my_dinner.count()
    dinner_list = []
    for item in my_dinner:
        dinner_list.append(item.fooditem.all())
    dinner_view_list = []
    for items in dinner_list:
        for dn_food in items:
            dinner_view_list.append(dn_food)

    snacks = Category.objects.filter(name='snacks')[0].userfooditem_set.all()
    my_snacks = snacks.filter(customer=cust)
    scnt = my_snacks.count()
    snacks_list = []
    for item in my_snacks:
        snacks_list.append(item.fooditem.all())
    snacks_view_list = []
    for items in snacks_list:
        for sn_food in items:
            snacks_view_list.append(sn_food)

    fooditems = FoodItem.objects.filter()

    total = UserFoodItem.objects.all()

    myfooditems = total.filter(customer=cust)

    today_date = date.today()

    cnt = myfooditems.count()
    querysetFood = []
    add_date_list = []
    for food in myfooditems:
        querysetFood.append(food.fooditem.all())
        add_date_list.append(food.add_date)
    finalFoodItems = []
    for items in querysetFood:
        for food_items in items:
            finalFoodItems.append(food_items)
    totalCalories = 0
    dailyCalories = user.calories_per_day()
    for foods in finalFoodItems:
        totalCalories += foods.calorie
    CalorieLeft = dailyCalories - totalCalories

    context = {'CalorieLeft': CalorieLeft, 'totalCalories': totalCalories, 'cnt': cnt, 'foodlist': finalFoodItems,
               'fooditem': fooditems, 'today_date': today_date, 'add_date': add_date_list,
               'breakfast': breakfast_view_list,
               'bcnt': bcnt,
               'lcnt': lcnt,
               'scnt': scnt,
               'dcnt': dcnt,
               'lunch': lunch_view_list,
               'dinner': dinner_view_list,
               'snacks': snacks_view_list,}
    return render(request, 'user_calc.html', context)

@login_required
def addFooditem_breakfast(request):
    user = request.user
    if request.method == "POST":
        form = AddUserFoodItem_breakfast(request.POST, initial={'customer':  user})
        if form.is_valid():
            form.save()
            return redirect('/calories_calc/user_calc/')
    form = AddUserFoodItem_breakfast(initial={'customer':  user})
    context = {'form': form}
    return render(request, 'AddUserFoodItem.html', context)

@login_required
def addFooditem_lunch(request):
    user = request.user
    if request.method == "POST":
        form = AddUserFoodItem_lunch(request.POST, initial={'customer':  user})
        if form.is_valid():
            form.save()
            return redirect('/calories_calc/user_calc/')
    form = AddUserFoodItem_lunch(initial={'customer':  user})
    context = {'form': form}
    return render(request, 'AddUserFoodItem.html', context)

@login_required
def addFooditem_dinner(request):
    user = request.user
    if request.method == "POST":
        form = AddUserFoodItem_dinner(request.POST, initial={'customer':  user})
        if form.is_valid():
            form.save()
            return redirect('/calories_calc/user_calc/')
    form = AddUserFoodItem_dinner(initial={'customer':  user})
    context = {'form': form}
    return render(request, 'AddUserFoodItem.html', context)

@login_required
def addFooditem_snacks(request):
    user = request.user
    if request.method == "POST":
        form = AddUserFoodItem_snacks(request.POST, initial={'customer':  user})
        if form.is_valid():
            form.save()
            return redirect('/calories_calc/user_calc/')
    form = AddUserFoodItem_snacks(initial={'customer':  user})
    context = {'form': form}
    return render(request, 'AddUserFoodItem.html', context)

@login_required
def deleteFooditem_all(request):
    user = request.user
    cust = user.id
    total = UserFoodItem.objects.all()

    myfooditems = total.filter(customer=cust)
    myfooditems.delete()
    return redirect('/calories_calc/user_calc/')

@login_required
def deleteFooditem_breakfast(request):
    user = request.user
    cust = user.id
    breakfast = Category.objects.filter(name='breakfast')[0].userfooditem_set.all()
    my_breakfast = breakfast.filter(customer=cust)

    my_breakfast_reverse = my_breakfast[::-1]
    my_breakfast_reverse[0].delete()
    return redirect('/calories_calc/user_calc/')

@login_required
def deleteFooditem_lunch(request):
    user = request.user
    cust = user.id
    lunch = Category.objects.filter(name='lunch')[0].userfooditem_set.all()
    my_lunch = lunch.filter(customer=cust)

    my_lunch_reverse = my_lunch[::-1]
    my_lunch_reverse[0].delete()
    return redirect('/calories_calc/user_calc/')

@login_required
def deleteFooditem_dinner(request):
    user = request.user
    cust = user.id
    dinner = Category.objects.filter(name='dinner')[0].userfooditem_set.all()
    my_dinner = dinner.filter(customer=cust)

    my_dinner_reverse = my_dinner[::-1]
    my_dinner_reverse[0].delete()
    return redirect('/calories_calc/user_calc/')

@login_required
def deleteFooditem_snacks(request):
    user = request.user
    cust = user.id
    snacks = Category.objects.filter(name='snacks')[0].userfooditem_set.all()
    my_snacks = snacks.filter(customer=cust)

    my_snacks_reverse = my_snacks[::-1]
    my_snacks_reverse[0].delete()
    return redirect('/calories_calc/user_calc/')





