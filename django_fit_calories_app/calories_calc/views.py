from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import FoodItem, UserFoodItem, ChooseDate
from .forms import FoodItemForm
from datetime import date
from decimal import Decimal

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

    fooditems = FoodItem.objects.filter()
    total = UserFoodItem.objects.all()

    quantity_list = []
    for i in total:
        food_quantity = i.quantity
        quantity_list.append(food_quantity)

    ch_date = ChooseDate.objects.all()
    ch_dt_list = []
    for dt in ch_date:
        ch_dt_list.clear()
        ch_dt_list.append(dt.c_date)

    main_date = ch_dt_list[0]

    breakfast = Category.objects.filter(name='breakfast')[0].userfooditem_set.all()
    my_breakfast = breakfast.filter(customer=cust, add_date=main_date)
    bcnt = my_breakfast.count()
    breakfast_list = []
    breakfast_quantity_list = []
    for item in my_breakfast:
        breakfast_list.append(item.fooditem.all())
        breakfast_quantity_list.append(item.quantity)
    breakfast_view_list = []
    for items in breakfast_list:
        for br_food in items:
            breakfast_view_list.append(br_food)

    if len(breakfast_view_list) > 0:
        for i in range(len(breakfast_quantity_list)):
            breakfast_view_list[i].calorie *= Decimal(breakfast_quantity_list[i]) / 100
            breakfast_view_list[i].calorie = breakfast_view_list[i].calorie.quantize(Decimal("1.00"))

            breakfast_view_list[i].protein *= Decimal(breakfast_quantity_list[i]) / 100
            breakfast_view_list[i].protein = breakfast_view_list[i].protein.quantize(Decimal("1.00"))

            breakfast_view_list[i].fats *= Decimal(breakfast_quantity_list[i]) / 100
            breakfast_view_list[i].fats = breakfast_view_list[i].fats.quantize(Decimal("1.00"))

            breakfast_view_list[i].carbohydrate *= Decimal(breakfast_quantity_list[i]) / 100
            breakfast_view_list[i].carbohydrate = breakfast_view_list[i].carbohydrate.quantize(Decimal("1.00"))

            breakfast_view_list[i].quantity *= Decimal(breakfast_quantity_list[i]) / 100
            breakfast_view_list[i].quantity = breakfast_view_list[i].quantity.quantize(Decimal("1.00"))

    lunch = Category.objects.filter(name='lunch')[0].userfooditem_set.all()
    my_lunch = lunch.filter(customer=cust, add_date=main_date)
    lcnt = my_lunch.count()
    lunch_list = []
    lunch_quantity_list = []
    for item in my_lunch:
        lunch_list.append(item.fooditem.all())
        lunch_quantity_list.append(item.quantity)
    lunch_view_list = []
    for items in lunch_list:
        for lc_food in items:
            lunch_view_list.append(lc_food)

    if len(lunch_view_list) > 0:
        for i in range(len(lunch_quantity_list)):
            lunch_view_list[i].calorie *= Decimal(lunch_quantity_list[i]) / 100
            lunch_view_list[i].calorie = lunch_view_list[i].calorie.quantize(Decimal("1.00"))

            lunch_view_list[i].protein *= Decimal(lunch_quantity_list[i]) / 100
            lunch_view_list[i].protein = lunch_view_list[i].protein.quantize(Decimal("1.00"))

            lunch_view_list[i].fats *= Decimal(lunch_quantity_list[i]) / 100
            lunch_view_list[i].fats = lunch_view_list[i].fats.quantize(Decimal("1.00"))

            lunch_view_list[i].carbohydrate *= Decimal(lunch_quantity_list[i]) / 100
            lunch_view_list[i].carbohydrate = lunch_view_list[i].carbohydrate.quantize(Decimal("1.00"))

            lunch_view_list[i].quantity *= Decimal(lunch_quantity_list[i]) / 100
            lunch_view_list[i].quantity = lunch_view_list[i].quantity.quantize(Decimal("1.00"))

    dinner = Category.objects.filter(name='dinner')[0].userfooditem_set.all()
    my_dinner = dinner.filter(customer=cust, add_date=main_date)
    dcnt = my_dinner.count()
    dinner_list = []
    dinner_quantity_list = []
    for item in my_dinner:
        dinner_list.append(item.fooditem.all())
        dinner_quantity_list.append(item.quantity)
    dinner_view_list = []
    for items in dinner_list:
        for dn_food in items:
            dinner_view_list.append(dn_food)

    if len(dinner_view_list) > 0:
        for i in range(len(dinner_quantity_list)):
            dinner_view_list[i].calorie *= Decimal(dinner_quantity_list[i]) / 100
            dinner_view_list[i].calorie = dinner_view_list[i].calorie.quantize(Decimal("1.00"))

            dinner_view_list[i].protein *= Decimal(dinner_quantity_list[i]) / 100
            dinner_view_list[i].protein = dinner_view_list[i].protein.quantize(Decimal("1.00"))

            dinner_view_list[i].fats *= Decimal(dinner_quantity_list[i]) / 100
            dinner_view_list[i].fats = dinner_view_list[i].fats.quantize(Decimal("1.00"))

            dinner_view_list[i].carbohydrate *= Decimal(dinner_quantity_list[i]) / 100
            dinner_view_list[i].carbohydrate = dinner_view_list[i].carbohydrate.quantize(Decimal("1.00"))

            dinner_view_list[i].quantity *= Decimal(dinner_quantity_list[i]) / 100
            dinner_view_list[i].quantity = dinner_view_list[i].quantity.quantize(Decimal("1.00"))

    snacks = Category.objects.filter(name='snacks')[0].userfooditem_set.all()
    my_snacks = snacks.filter(customer=cust, add_date=main_date)
    scnt = my_snacks.count()
    snacks_list = []
    snacks_quantity_list = []
    for item in my_snacks:
        snacks_list.append(item.fooditem.all())
        snacks_quantity_list.append(item.quantity)
    snacks_view_list = []
    for items in snacks_list:
        for sn_food in items:
            snacks_view_list.append(sn_food)

    if len(snacks_view_list) > 0:
        for i in range(len(snacks_quantity_list)):
            snacks_view_list[i].calorie *= Decimal(snacks_quantity_list[i]) / 100
            snacks_view_list[i].calorie = snacks_view_list[i].calorie.quantize(Decimal("1.00"))

            snacks_view_list[i].protein *= Decimal(snacks_quantity_list[i]) / 100
            snacks_view_list[i].protein = snacks_view_list[i].protein.quantize(Decimal("1.00"))

            snacks_view_list[i].fats *= Decimal(snacks_quantity_list[i]) / 100
            snacks_view_list[i].fats = snacks_view_list[i].fats.quantize(Decimal("1.00"))

            snacks_view_list[i].carbohydrate *= Decimal(snacks_quantity_list[i]) / 100
            snacks_view_list[i].carbohydrate = snacks_view_list[i].carbohydrate.quantize(Decimal("1.00"))

            snacks_view_list[i].quantity *= Decimal(snacks_quantity_list[i]) / 100
            snacks_view_list[i].quantity = snacks_view_list[i].quantity.quantize(Decimal("1.00"))

    myfooditems = total.filter(customer=cust, add_date=main_date)

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

    add_date_list_set = list(set(add_date_list))

    totalCalories = 0
    dailyCalories = user.calories_per_day()

    for foods in finalFoodItems:
        totalCalories += foods.calorie
    CalorieLeft = dailyCalories - totalCalories

    context = {'CalorieLeft': CalorieLeft, 'totalCalories': totalCalories, 'cnt': cnt, 'foodlist': finalFoodItems,
               'fooditem': fooditems, 'today_date': today_date, 'add_date': add_date_list_set,
               'add_date_list': add_date_list, 'main_date': main_date,
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
    ch_date = ChooseDate.objects.all()
    ch_dt_list = []
    for dt in ch_date:
        ch_dt_list.clear()
        ch_dt_list.append(dt.c_date)
    main_date = ch_dt_list[0]
    if request.method == "POST":
        form = AddUserFoodItem_breakfast(request.POST, initial={'customer':  user})
        if form.is_valid():
            form.save()
            return redirect('/calories_calc/user_calc/')
    form = AddUserFoodItem_breakfast(initial={'customer':  user, 'add_date': main_date})
    context = {'form': form, 'main_date': main_date}
    return render(request, 'AddUserFoodItem.html', context)

@login_required
def addFooditem_lunch(request):
    user = request.user
    ch_date = ChooseDate.objects.all()
    ch_dt_list = []
    for dt in ch_date:
        ch_dt_list.clear()
        ch_dt_list.append(dt.c_date)
    main_date = ch_dt_list[0]
    if request.method == "POST":
        form = AddUserFoodItem_lunch(request.POST, initial={'customer':  user})
        if form.is_valid():
            form.save()
            return redirect('/calories_calc/user_calc/')
    form = AddUserFoodItem_lunch(initial={'customer':  user, 'add_date': main_date})
    context = {'form': form, 'main_date': main_date}
    return render(request, 'AddUserFoodItem.html', context)

@login_required
def addFooditem_dinner(request):
    user = request.user
    ch_date = ChooseDate.objects.all()
    ch_dt_list = []
    for dt in ch_date:
        ch_dt_list.clear()
        ch_dt_list.append(dt.c_date)
    main_date = ch_dt_list[0]
    if request.method == "POST":
        form = AddUserFoodItem_dinner(request.POST, initial={'customer':  user})
        if form.is_valid():
            form.save()
            return redirect('/calories_calc/user_calc/')
    form = AddUserFoodItem_dinner(initial={'customer':  user, 'add_date': main_date})
    context = {'form': form, 'main_date': main_date}
    return render(request, 'AddUserFoodItem.html', context)

@login_required
def addFooditem_snacks(request):
    user = request.user
    ch_date = ChooseDate.objects.all()
    ch_dt_list = []
    for dt in ch_date:
        ch_dt_list.clear()
        ch_dt_list.append(dt.c_date)
    main_date = ch_dt_list[0]
    if request.method == "POST":
        form = AddUserFoodItem_snacks(request.POST, initial={'customer':  user})
        if form.is_valid():
            form.save()
            return redirect('/calories_calc/user_calc/')
    form = AddUserFoodItem_snacks(initial={'customer':  user, 'add_date': main_date})
    context = {'form': form, 'main_date': main_date}
    return render(request, 'AddUserFoodItem.html', context)

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

@login_required
def choose_date(request):
    today_date = date.today()
    if request.method == 'POST':
        form = ChooseDateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/calories_calc/user_calc/')
    form = ChooseDateForm()
    context = {
        'form': form, 'today_date': today_date,
    }

    return render(request, 'choose_date.html', context)




