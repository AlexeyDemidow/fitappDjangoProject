from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from .forms import *
from .models import UserFoodItem
from .pagination import ProductsPagination, UserProductsPagination, WaterTrackerPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import FoodItemSerializer, UserFoodItemSerializerRead, UserFoodItemSerializerWrite, \
    WaterTrackerSerializer
from .utils import *
from rest_framework import viewsets, status


class ProductsAPIViewSet(viewsets.ModelViewSet):
    """Вьюсет для работы с базой данных продуктов"""

    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    permission_classes = (IsAdminUser, )
    pagination_class = ProductsPagination


class UserProductsAPIViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для чтения пользовательских продуктами"""

    serializer_class = UserFoodItemSerializerRead
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated, )
    pagination_class = UserProductsPagination

    def get_queryset(self):
        user = self.request.user.id
        return UserFoodItem.objects.filter(customer=user).values(
            'id',
            'customer__username',
            'fooditem__name',
            'fooditem__protein',
            'fooditem__fats',
            'fooditem__carbohydrate',
            'fooditem__calorie',
            'category__name',
            'add_date',
            'quantity'
        )

    @action(detail=False, methods=['get'], url_path=r'(?P<dates>[0-9]{4}-?[0-9]{2}-?[0-9]{2})')
    def date_sort(self, request, dates):
        user = self.request.user.id
        today_list = UserFoodItem.objects.filter(customer=user, add_date=dates).values(
            'id',
            'customer__username',
            'fooditem__name',
            'fooditem__protein',
            'fooditem__fats',
            'fooditem__carbohydrate',
            'fooditem__calorie',
            'category__name',
            'add_date',
            'quantity'
        )

        page = self.paginate_queryset(today_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(today_list, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path=r'(?P<dates>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/(?P<meal>[a-z]+)')
    def meals(self, request, dates, meal):
        user = self.request.user.id
        category = Category.objects.filter(name=meal).first()
        if not category:
            return Response({'error': 'Нет такой категории.'}, status=status.HTTP_404_NOT_FOUND)
        today_list = [UserFoodItem.objects.filter(customer=user, category=category, add_date=dates).values(
            'id',
            'customer__username',
            'fooditem__name',
            'fooditem__protein',
            'fooditem__fats',
            'fooditem__carbohydrate',
            'fooditem__calorie',
            'category__name',
            'add_date',
            'quantity'
        ) for category in [category]]
        page = self.paginate_queryset(today_list[0])
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(today_list[0], many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path=r'(?P<dates>[0-9]{4}-?[0-9]{2}-?[0-9]{2})/daily_statistics')
    def statistics(self, request, dates):
        user = self.request.user.id
        today_list = UserFoodItem.objects.filter(customer=user, add_date=dates)

        product_counter = len(today_list)
        norm_calories = [i.get('calories') for i in CustomUser.objects.filter(id=user).values('calories')][0]
        if norm_calories == 0:
            norm_calories = CustomUser.calories_per_day(CustomUser.objects.get(id=user))

        quantity = [i.get('quantity') for i in today_list.values('quantity')]
        fooditem_calories = [i.get('fooditem__calorie') / 100 for i in UserFoodItem.objects.filter(
            customer=user,
            add_date=dates
        ).values('fooditem__calorie')]
        calories_counter = []
        for k in range(len(quantity)):
            cal = quantity[k] * fooditem_calories[k]
            calories_counter.append(cal)
        calories_counter = round(sum(calories_counter), 2)

        remaining_calories_counter = norm_calories - calories_counter

        fooditem_protein = [i.get('fooditem__protein') / 100 for i in UserFoodItem.objects.filter(
            customer=user,
            add_date=dates
        ).values('fooditem__protein')]
        protein_counter = []
        for k in range(len(quantity)):
            prot = quantity[k] * fooditem_protein[k]
            protein_counter.append(prot)
        protein_counter = round(sum(protein_counter), 2)

        fooditem_fats = [i.get('fooditem__fats') / 100 for i in
                            UserFoodItem.objects.filter(customer=user, add_date=dates).values('fooditem__fats')]
        fats_counter = []
        for k in range(len(quantity)):
            fats = quantity[k] * fooditem_fats[k]
            fats_counter.append(fats)
        fats_counter = round(sum(fats_counter), 2)

        fooditem_carb = [i.get('fooditem__carbohydrate') / 100 for i in
                         UserFoodItem.objects.filter(customer=user, add_date=dates).values('fooditem__carbohydrate')]
        carb_counter = []
        for k in range(len(quantity)):
            carb = quantity[k] * fooditem_carb[k]
            carb_counter.append(carb)
        carb_counter = round(sum(carb_counter), 2)

        context = {
            'all_products': product_counter,
            'norm_calories': norm_calories,
            'calories_counter': calories_counter,
            'remaining_calories_counter': remaining_calories_counter,
            'protein_counter': protein_counter,
            'fats_counter': fats_counter,
            'carb_counter': carb_counter,
        }
        return Response(context)


class UserProductsAPIViewSetWrite(viewsets.ModelViewSet):
    """Вьюсет для редактирования пользовательских продуктами"""

    serializer_class = UserFoodItemSerializerWrite
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated, )
    pagination_class = UserProductsPagination

    def get_queryset(self):
        user = self.request.user.id
        return UserFoodItem.objects.filter(customer=user)


class WaterTrackerAPIViewSet(viewsets.ModelViewSet):
    """Вьюсет для трекера воды"""

    serializer_class = WaterTrackerSerializer
    pagination_class = WaterTrackerPagination
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user.id
        return WaterTracker.objects.filter(customer=user)

    @action(detail=False, methods=['get'], url_path=r'(?P<dates>[0-9]{4}-?[0-9]{2}-?[0-9]{2})')
    def all_glasses(self, request, dates):
        user = self.request.user.id
        water_tracker_list = WaterTracker.objects.filter(customer=user, drink_date=dates)
        glass_counter = 0
        for i in water_tracker_list.values('glass'):
            glass_counter += i.get('glass')
        return Response({'all_glasses': glass_counter})
