from django.urls import path, include
from . import views




urlpatterns = [

    path('calc_main/', views.calc_main, name='calc_main'),
    path('product/', views.fooditem, name='fooditem'),
    path('user_calc/createfooditem/', views.createfooditem, name='createfooditem'),
    path('user_calc/addFooditem/', views.addFooditem, name='addFooditem'),
    path('user_calc/', views.user_calc, name='user_calc'),
    path('user_calc/deleteFooditem', views.deleteFooditem, name='deleteFooditem'),
]


#<str:name>