from django.urls import path
from . import views


urlpatterns = [
    path('user_calc/', views.user_calc, name='user_calc'),  # Трекер калорий
    path('user_calc/delete_food_item/<int:item_id>', views.delete_food_item, name='delete_food_item'),  # Удаление пищи из таблицы трекера калорий
    path('upload_csv/', views.upload_csv, name='upload_csv'),  # Загрузка CSV файла с базой данных продуктов
    path('show_imported_products/', views.show_imported_products, name='show_imported_products'),  # Показать импортированные продукты
    path('charts/', views.charts, name='charts'),  # Статистика
]
