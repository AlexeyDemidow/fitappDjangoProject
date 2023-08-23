from django.urls import path
from .views import SignUpView
from .views import profile
from .views import edit_profile


from django.contrib.auth import views


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<str:username>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('<str:username>/', profile, name='profile'),
    path('<str:username>/edit_profile', edit_profile, name='edit_profile'),

]
