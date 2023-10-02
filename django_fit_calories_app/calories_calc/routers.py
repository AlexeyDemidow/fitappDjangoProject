from rest_framework import routers

from calories_calc.views import ProductsAPIViewSet, UserProductsAPIViewSet, UserProductsAPIViewSetWrite

# Роутер для базы данных продуктов
food_item_router = routers.SimpleRouter()
food_item_router.register(r'foodlist', ProductsAPIViewSet)

# Роутер для базы данных пользовательских продуктов
read_user_food_item_router = routers.SimpleRouter()
read_user_food_item_router.register(r'user_foodlist', UserProductsAPIViewSet)

write_user_food_item_router = routers.SimpleRouter()
write_user_food_item_router.register(r'user_foodlist_edit', UserProductsAPIViewSetWrite)

# print(user_food_item_router.urls)
