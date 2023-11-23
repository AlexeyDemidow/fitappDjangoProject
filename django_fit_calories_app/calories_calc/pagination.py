from rest_framework.pagination import PageNumberPagination


class ProductsPagination(PageNumberPagination):
    """Пагинация для базы данных продуктов"""

    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10000


class UserProductsPagination(PageNumberPagination):
    """Пагинация для пользовательских продуктов"""

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10000


class WaterTrackerPagination(PageNumberPagination):
    """Пагинация для трекера воды"""

    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 10000
