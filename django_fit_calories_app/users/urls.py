from django.urls import path
from .views import *
from django.contrib.auth import views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),  # Регистрация
    path('signup_success/', signup_success, name='signup_success'),  # Сигнал об успешной регистрации
    path('login/', views.LoginView.as_view(redirect_authenticated_user=True), name='user_login'),  # Вход
    path('logout/', views.LogoutView.as_view(), name='user_logout'),  # Выход
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),  # Смена пароля
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # Сигнал о смене пароля
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Подтверждение смены пароля
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  # Сигнал об успешной смене пароля
    path('<str:username>/', profile, name='profile'),  # Профиль пользователя
    path('<str:username>/edit_profile', edit_profile, name='edit_profile'),  # Редактирование профиля

]
