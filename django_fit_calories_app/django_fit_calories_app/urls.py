"""
URL configuration for django_fit_calories_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from calories_calc.routers import food_item_router, read_user_food_item_router, write_user_food_item_router, \
    water_tracker_router
from users.routers import admin_profiles_edit_router, profile_router, weighing_router

# from users.views import CreateProfileAPIView, ProfileAPIView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Главная
    path('admin/', admin.site.urls),  # Админ
    path('users/', include('users.urls')),  # Профиль
    path('calories_calc/', include('calories_calc.urls')),  # Трекер

    path('api/v1/api-auth/', include('rest_framework.urls')),  # Авторизация на основе сессий cookies
    path('api/v1/auth/', include('djoser.urls')),  # Авторизация djoser
    path('api/v1/auth/', include('djoser.urls.authtoken')),  # Авторизация djoser
    path('api/v1/auth/', include('djoser.urls.jwt')),  # Авторизация djoser
    path('api/v1/', include(food_item_router.urls)),  # Работа с базой данных продуктов
    path('api/v1/', include(read_user_food_item_router.urls)),  # Работа с базой данных пользовательских продуктов
    path('api/v1/', include(write_user_food_item_router.urls)),  # Работа с базой данных пользовательских продуктов
    path('api/v1/', include(water_tracker_router.urls)),  # Работа с трекером воды
    path('api/v1/', include(admin_profiles_edit_router.urls)),  # Работа с профилем пользователя
    path('api/v1/', include(profile_router.urls)),  # Работа с профилем пользователя
    path('api/v1/', include(weighing_router.urls)),  # Работа с профилем пользователя
    # path('api/v1/profile/<int:id>', ProfileAPIView.as_view()),  # Работа с профилем пользователя
    # path('api/v1/profile/create/', CreateProfileAPIView.as_view()),  # Работа с профилем пользователя

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
