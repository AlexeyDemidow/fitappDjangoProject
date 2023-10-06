from rest_framework.pagination import PageNumberPagination


# Пагинация для базы данных продуктов
class ProductsPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000


# Пагинация для пользовательских продуктов
class UserProductsPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000


# Пагинация для трекера воды
class WaterTrackerPagination(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 10000