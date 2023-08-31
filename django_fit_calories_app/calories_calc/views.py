from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import FoodItem, UserFoodItem, ChooseDate
from .forms import CSVupload
from calories_calc.utils import import_products_from_csv
from datetime import date
from decimal import Decimal

# Create your views here.


@login_required
def user_calc(request):
    user = request.user
    cust = user.id
    total = UserFoodItem.objects.all()

    quantity_list = []
    for f_quan in total:
        food_quantity = f_quan.quantity
        quantity_list.append(food_quantity)

    ch_date = ChooseDate.objects.all()
    ch_dt_list = [date.today()]
    for dt in ch_date:
        ch_dt_list.clear()
        ch_dt_list.append(dt.c_date)

    main_date = ch_dt_list[0]
    today_date = date.today()

    if request.method == 'POST':
        form_drink = WaterTrackerForm(request.POST, initial={'customer': user})
        if form_drink.is_valid():
            form_drink.save()
            return redirect('user_calc')
    form_drink = WaterTrackerForm(initial={'customer': user, 'drink_date': main_date})

    w = WaterTracker.objects.filter(customer=user, drink_date=main_date)
    water_count = 0
    for ww in w:
        water_count += ww.glass

    if request.method == 'POST':
        createfooditemform = FoodItemForm(request.POST)
        if createfooditemform.is_valid():
            createfooditemform.save()
            return redirect('/calories_calc/user_calc/')
    createfooditemform = FoodItemForm(request.POST)

    breakfast = Category.objects.filter(name='breakfast')[0].userfooditem_set.all()
    my_breakfast = breakfast.filter(customer=cust, add_date=main_date)
    bcnt = my_breakfast.count()
    breakfast_list = []
    breakfast_list_id = []
    breakfast_quantity_list = []
    for item in my_breakfast:
        breakfast_list.append(item.fooditem.all())
        breakfast_list_id.append(item.id)
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

    breakfast_view_dict = {}
    for d_index in range(len(breakfast_view_list)):
        breakfast_view_dict[breakfast_list_id[d_index]] = breakfast_view_list[d_index]

    calorie_count_br = 0
    protein_count_br = 0
    fats_count_br = 0
    carbohydrate_count_br = 0
    quantity_count_br = 0
    for j in range(len(breakfast_view_list)):
        calorie_count_br += breakfast_view_list[j].calorie
        protein_count_br += breakfast_view_list[j].protein
        fats_count_br += breakfast_view_list[j].fats
        carbohydrate_count_br += breakfast_view_list[j].carbohydrate
        quantity_count_br += breakfast_view_list[j].quantity

    lunch = Category.objects.filter(name='lunch')[0].userfooditem_set.all()
    my_lunch = lunch.filter(customer=cust, add_date=main_date)
    lcnt = my_lunch.count()
    lunch_list = []
    lunch_quantity_list = []
    lunch_list_id = []
    for item in my_lunch:
        lunch_list.append(item.fooditem.all())
        lunch_list_id.append(item.id)
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

    lunch_view_dict = {}
    for d_index in range(len(lunch_view_list)):
        lunch_view_dict[lunch_list_id[d_index]] = lunch_view_list[d_index]

    calorie_count_lu = 0
    protein_count_lu = 0
    fats_count_lu = 0
    carbohydrate_count_lu = 0
    quantity_count_lu = 0
    for j in range(len(lunch_view_list)):
        calorie_count_lu += lunch_view_list[j].calorie
        protein_count_lu += lunch_view_list[j].protein
        fats_count_lu += lunch_view_list[j].fats
        carbohydrate_count_lu += lunch_view_list[j].carbohydrate
        quantity_count_lu += lunch_view_list[j].quantity

    dinner = Category.objects.filter(name='dinner')[0].userfooditem_set.all()
    my_dinner = dinner.filter(customer=cust, add_date=main_date)
    dcnt = my_dinner.count()
    dinner_list = []
    dinner_list_id = []
    dinner_quantity_list = []
    for item in my_dinner:
        dinner_list.append(item.fooditem.all())
        dinner_list_id.append(item.id)
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

    dinner_view_dict = {}
    for d_index in range(len(dinner_view_list)):
        dinner_view_dict[dinner_list_id[d_index]] = dinner_view_list[d_index]

    calorie_count_di = 0
    protein_count_di = 0
    fats_count_di = 0
    carbohydrate_count_di = 0
    quantity_count_di = 0
    for j in range(len(dinner_view_list)):
        calorie_count_di += dinner_view_list[j].calorie
        protein_count_di += dinner_view_list[j].protein
        fats_count_di += dinner_view_list[j].fats
        carbohydrate_count_di += dinner_view_list[j].carbohydrate
        quantity_count_di += dinner_view_list[j].quantity

    snacks = Category.objects.filter(name='snacks')[0].userfooditem_set.all()
    my_snacks = snacks.filter(customer=cust, add_date=main_date)
    scnt = my_snacks.count()
    snacks_list = []
    snacks_list_id = []
    snacks_quantity_list = []
    for item in my_snacks:
        snacks_list.append(item.fooditem.all())
        snacks_list_id.append(item.id)
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

    snacks_view_dict = {}
    for d_index in range(len(snacks_view_list)):
        snacks_view_dict[snacks_list_id[d_index]] = snacks_view_list[d_index]

    calorie_count_sn = 0
    protein_count_sn = 0
    fats_count_sn = 0
    carbohydrate_count_sn = 0
    quantity_count_sn = 0
    for j in range(len(snacks_view_list)):
        calorie_count_sn += snacks_view_list[j].calorie
        protein_count_sn += snacks_view_list[j].protein
        fats_count_sn += snacks_view_list[j].fats
        carbohydrate_count_sn += snacks_view_list[j].carbohydrate
        quantity_count_sn += snacks_view_list[j].quantity

    calorie_count_all = calorie_count_br + calorie_count_lu + calorie_count_di + calorie_count_sn
    protein_count_all = protein_count_br + protein_count_lu + protein_count_di + protein_count_sn
    fats_count_all = fats_count_br + fats_count_lu + fats_count_di + fats_count_sn
    carbohydrate_count_all = carbohydrate_count_br + carbohydrate_count_lu + carbohydrate_count_di + carbohydrate_count_sn
    quantity_count_all = quantity_count_br + quantity_count_lu + quantity_count_di + quantity_count_sn

    if request.method == "POST":
        form_br = AddUserFoodItem_breakfast(request.POST, initial={'customer':  user})
        if form_br.is_valid():
            form_br.save()
            return redirect('/calories_calc/user_calc/')
    form_br = AddUserFoodItem_breakfast(initial={'customer': user, 'add_date': main_date})

    if request.method == "POST":
        form_lu = AddUserFoodItem_lunch(request.POST, initial={'customer': user})
        if form_lu.is_valid():
            form_lu.save()
            return redirect('/calories_calc/user_calc/')
    form_lu = AddUserFoodItem_lunch(initial={'customer': user, 'add_date': main_date})

    if request.method == "POST":
        form_di = AddUserFoodItem_dinner(request.POST, initial={'customer':  user})
        if form_di.is_valid():
            form_di.save()
            return redirect('/calories_calc/user_calc/')
    form_di = AddUserFoodItem_dinner(initial={'customer': user, 'add_date': main_date})

    if request.method == "POST":
        form_sn = AddUserFoodItem_snacks(request.POST, initial={'customer':  user})
        if form_sn.is_valid():
            form_sn.save()
            return redirect('/calories_calc/user_calc/')
    form_sn = AddUserFoodItem_snacks(initial={'customer': user, 'add_date': main_date})

    if request.method == 'POST':
        form_ch = ChooseDateForm(request.POST)
        if form_ch.is_valid():
            form_ch.save()
            return redirect('/calories_calc/user_calc/')
    form_ch = ChooseDateForm()

    context = {'main_date': main_date, 'today_date': today_date,

               'breakfast': breakfast_view_list, 'breakfast_view_dict': breakfast_view_dict, 'bcnt': bcnt,
               'lunch': lunch_view_list, 'lunch_view_dict': lunch_view_dict, 'lcnt': lcnt,
               'dinner': dinner_view_list, 'dinner_view_dict': dinner_view_dict, 'dcnt': dcnt,
               'snacks': snacks_view_list, 'snacks_view_dict': snacks_view_dict, 'scnt': scnt,

               'my_breakfast': my_breakfast, 'createfooditemform': createfooditemform,

               'form_br': form_br, 'form_lu': form_lu, 'form_di': form_di, 'form_sn': form_sn,
               'form_ch': form_ch, 'form_drink': form_drink, 'water_count': water_count,

               'calorie_count_sn': calorie_count_sn,
               'protein_count_sn': protein_count_sn,
               'fats_count_sn': fats_count_sn,
               'carbohydrate_count_sn': carbohydrate_count_sn,
               'quantity_count_sn': quantity_count_sn,

               'calorie_count_br': calorie_count_br,
               'protein_count_br': protein_count_br,
               'fats_count_br': fats_count_br,
               'carbohydrate_count_br': carbohydrate_count_br,
               'quantity_count_br': quantity_count_br,

               'calorie_count_lu': calorie_count_lu,
               'protein_count_lu': protein_count_lu,
               'fats_count_lu': fats_count_lu,
               'carbohydrate_count_lu': carbohydrate_count_lu,
               'quantity_count_lu': quantity_count_lu,

               'calorie_count_di': calorie_count_di,
               'protein_count_di': protein_count_di,
               'fats_count_di': fats_count_di,
               'carbohydrate_count_di': carbohydrate_count_di,
               'quantity_count_di': quantity_count_di,

               'calorie_count_all': calorie_count_all,
               'protein_count_all': protein_count_all,
               'fats_count_all': fats_count_all,
               'carbohydrate_count_all': carbohydrate_count_all,
               'quantity_count_all': quantity_count_all,

    }
    return render(request, 'user_calc.html', context)

@login_required
def deleteFooditem(request, item_id):
    item = get_object_or_404(UserFoodItem, id=item_id)
    item.delete()

    return redirect('/calories_calc/user_calc/')


@staff_member_required
def upload_csv(request):
    if request.method == 'POST':
        form = CSVupload(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            imported_products = import_products_from_csv(csv_file)
            request.session['imported_products'] = imported_products
            return redirect('show_imported_products')
    else:
        form = CSVupload()
    return render(request, 'upload_csv.html', {'form': form})

@staff_member_required
def show_imported_products(request):
    imported_products = request.session.get('imported_products', [])
    return render(request, 'imported_products.html', {'imported_products': imported_products})

@login_required
def charts(request):
    user = request.user
    cust = user.id

    ch_date = ChooseDate.objects.all()
    ch_dt_list = []
    for dt in ch_date:
        ch_dt_list.clear()
        ch_dt_list.append(dt.c_date)
    main_date = ch_dt_list[0]

    breakfast = Category.objects.filter(name='breakfast')[0].userfooditem_set.all()
    my_breakfast = breakfast.filter(customer=cust, add_date=main_date)
    breakfast_list = []
    for item in my_breakfast:
        breakfast_list.append(item.fooditem.all())
    breakfast_view_list = []
    for items in breakfast_list:
        for br_food in items:
            breakfast_view_list.append(br_food)

    calorie_count_br = 0
    protein_count_br = 0
    fats_count_br = 0
    carbohydrate_count_br = 0
    quantity_count_br = 0
    for j in range(len(breakfast_view_list)):
        calorie_count_br += breakfast_view_list[j].calorie
        protein_count_br += breakfast_view_list[j].protein
        fats_count_br += breakfast_view_list[j].fats
        carbohydrate_count_br += breakfast_view_list[j].carbohydrate
        quantity_count_br += breakfast_view_list[j].quantity

    lunch = Category.objects.filter(name='lunch')[0].userfooditem_set.all()
    my_lunch = lunch.filter(customer=cust, add_date=main_date)
    lunch_list = []
    for item in my_lunch:
        lunch_list.append(item.fooditem.all())
    lunch_view_list = []
    for items in lunch_list:
        for lc_food in items:
            lunch_view_list.append(lc_food)

    calorie_count_lu = 0
    protein_count_lu = 0
    fats_count_lu = 0
    carbohydrate_count_lu = 0
    quantity_count_lu = 0
    for j in range(len(lunch_view_list)):
        calorie_count_lu += lunch_view_list[j].calorie
        protein_count_lu += lunch_view_list[j].protein
        fats_count_lu += lunch_view_list[j].fats
        carbohydrate_count_lu += lunch_view_list[j].carbohydrate
        quantity_count_lu += lunch_view_list[j].quantity

    dinner = Category.objects.filter(name='dinner')[0].userfooditem_set.all()
    my_dinner = dinner.filter(customer=cust, add_date=main_date)
    dinner_list = []
    for item in my_dinner:
        dinner_list.append(item.fooditem.all())
    dinner_view_list = []
    for items in dinner_list:
        for dn_food in items:
            dinner_view_list.append(dn_food)

    calorie_count_di = 0
    protein_count_di = 0
    fats_count_di = 0
    carbohydrate_count_di = 0
    quantity_count_di = 0
    for j in range(len(dinner_view_list)):
        calorie_count_di += dinner_view_list[j].calorie
        protein_count_di += dinner_view_list[j].protein
        fats_count_di += dinner_view_list[j].fats
        carbohydrate_count_di += dinner_view_list[j].carbohydrate
        quantity_count_di += dinner_view_list[j].quantity

    snacks = Category.objects.filter(name='snacks')[0].userfooditem_set.all()
    my_snacks = snacks.filter(customer=cust, add_date=main_date)
    snacks_list = []
    for item in my_snacks:
        snacks_list.append(item.fooditem.all())
    snacks_view_list = []
    for items in snacks_list:
        for sn_food in items:
            snacks_view_list.append(sn_food)

    calorie_count_sn = 0
    protein_count_sn = 0
    fats_count_sn = 0
    carbohydrate_count_sn = 0
    quantity_count_sn = 0
    for j in range(len(snacks_view_list)):
        calorie_count_sn += snacks_view_list[j].calorie
        protein_count_sn += snacks_view_list[j].protein
        fats_count_sn += snacks_view_list[j].fats
        carbohydrate_count_sn += snacks_view_list[j].carbohydrate
        quantity_count_sn += snacks_view_list[j].quantity

    food_nutrients_labels = ['Белки', 'Жиры', 'Углеводы']
    data_breakfast = [float(protein_count_br), float(fats_count_br), float(carbohydrate_count_br)]
    data_lunch = [float(protein_count_lu), float(fats_count_lu), float(carbohydrate_count_lu)]
    data_dinner = [float(protein_count_di), float(fats_count_di), float(carbohydrate_count_di)]
    data_snacks = [float(protein_count_sn), float(fats_count_sn), float(carbohydrate_count_sn)]

    food_category_labels = ['Завтрак', 'Обед', 'Ужин', 'Перекусы']
    food_category_data = [float(calorie_count_br), float(calorie_count_lu), float(calorie_count_di), float(calorie_count_sn)]

    total = UserFoodItem.objects.all()
    myfooditems = total.filter(customer=cust, add_date=main_date)
    cnt = myfooditems.count()

    totalCalories = 0
    if user.calories > 0:
        dailyCalories = user.calories
    else:
        dailyCalories = user.calories_per_day()
    querysetFood = []

    add_date_list = []
    for food in myfooditems:
        querysetFood.append(food.fooditem.all())
        add_date_list.append(food.add_date)
    finalFoodItems = []
    for items in querysetFood:
        for food_items in items:
            finalFoodItems.append(food_items)

    for foods in finalFoodItems:
        totalCalories += foods.calorie
    CalorieLeft = dailyCalories - totalCalories

    if request.method == 'POST':
        form_ch = ChooseDateForm(request.POST)
        if form_ch.is_valid():
            form_ch.save()
            return redirect('charts')
    form_ch = ChooseDateForm()

    w = WaterTracker.objects.filter(customer=user, drink_date=main_date)
    water_count = 0
    for ww in w:
        water_count += ww.glass

    context = {
        'food_nutrients_labels': food_nutrients_labels, 'food_category_labels': food_category_labels,
        'food_category_data': food_category_data,
        'data_breakfast': data_breakfast,
        'data_lunch': data_lunch,
        'data_dinner': data_dinner,
        'data_snacks': data_snacks,
        'main_date': main_date,
        'form_ch': form_ch,
        'cnt': cnt,
        'CalorieLeft': CalorieLeft, 'totalCalories': totalCalories,
        'water_count': water_count,
    }

    return render(request, 'home.html', context)

# def drink_counter(request):
#     user = request.user
#
#     if request.method == 'POST':
#         form_drink = WaterTrackerForm(request.POST, initial={'customer': user})
#         if form_drink.is_valid():
#             form_drink.save()
#             return redirect('charts')
#     form_drink = WaterTrackerForm(initial={'customer': user})
#     context = {'form_drink': form_drink,}
#     return render(request, 'drink.html', context)
