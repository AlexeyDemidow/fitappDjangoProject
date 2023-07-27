from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.


from .forms import CustomUserCreationForm, CustomUserChangeFormAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeFormAdmin
    model = CustomUser
    list_display = ['username', 'email', 'gender', 'birth_date', 'growth', 'weight', 'avatar', 'activity']
    list_filter = ['is_active', 'is_staff', 'gender']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Информация', {'fields': ('email',)}),
        ('Разрешения', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Даты', {'fields': ('last_login', 'date_joined')}),
        ('Профиль', {'fields': ('gender', 'birth_date', 'growth', 'weight', 'avatar', 'activity')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            'username', 'email', 'gender', 'birth_date', 'growth', 'weight', 'avatar', 'activity',
            'password1', 'password2')}
         ),
    )
    search_fields = ('username', 'email',)
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)