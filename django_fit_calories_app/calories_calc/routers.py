from rest_framework import routers

from calories_calc.API_views import ProductsAPIViewSet, UserProductsAPIViewSet, UserProductsAPIViewSetWrite, \
    WaterTrackerAPIViewSet

# Роутер для базы данных продуктов
food_item_router = routers.SimpleRouter()
food_item_router.register(r'foodlist', ProductsAPIViewSet)

# Роутер для базы данных пользовательских продуктов
read_user_food_item_router = routers.SimpleRouter()
read_user_food_item_router.register(r'user_foodlist',
                                    UserProductsAPIViewSet,
                                    basename='user_foodlist'
                                    )
write_user_food_item_router = routers.SimpleRouter()
# Используем basename из-за того что querryset задан функцией
write_user_food_item_router.register(r'user_foodlist_edit',
                                     UserProductsAPIViewSetWrite,
                                     basename='user_foodlist_edit'
                                     )

# Роутер трекера воды
water_tracker_router = routers.SimpleRouter()
water_tracker_router.register(r'water_tracker',
                              WaterTrackerAPIViewSet,
                              basename='water_tracker')
