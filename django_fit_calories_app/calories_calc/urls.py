from django.urls import path
from . import views

urlpatterns = [
    path('user_calc/createfooditem/', views.createfooditem, name='createfooditem'),

    path('user_calc/addFooditem_breakfast/', views.addFooditem_breakfast, name='addFooditem_breakfast'),
    path('user_calc/addFooditem_lunch/', views.addFooditem_lunch, name='addFooditem_lunch'),
    path('user_calc/addFooditem_dinner/', views.addFooditem_dinner, name='addFooditem_dinner'),
    path('user_calc/addFooditem_snacks/', views.addFooditem_snacks, name='addFooditem_snacks'),

    path('user_calc/', views.user_calc, name='user_calc'),
    path('user_calc/deleteFooditem/<int:item_id>', views.deleteFooditem, name='deleteFooditem'),

    path('upload_csv/', views.upload_csv, name='upload_csv'),
    path('show_imported_products/', views.show_imported_products, name='show_imported_products'),

    path('charts/', views.charts, name='charts'),
]
