# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeFormAdmin
from .models import CustomUser, Weighing


# Модель пользователя в админ панели
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
            'fields': ('username', 'email', 'gender', 'birth_date', 'growth', 'weight', 'avatar', 'activity',
                       'password1', 'password2')}
         ),
    )
    search_fields = ('username', 'email',)
    ordering = ('username',)


# Модель данных о взвешивании в админ панели
class UserWeighing(admin.ModelAdmin):
    class Meta:
        model = Weighing

    list_display = ['_user', 'weight_value', 'weighing_date']
    list_filter = ['weight_value', 'user', 'weighing_date']

    def _user(self, row):
        return ','.join([x.username for x in row.user.all()])


# Разделы в админ панели
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Weighing, UserWeighing)
