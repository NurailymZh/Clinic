# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import CustomUser
# from django.contrib import admin
# from . import models
# from django.contrib.auth.admin import UserAdmin

# class CustomUserAdmin(UserAdmin):
#     """Регистрация модели CustomUser в админ панели"""

#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
#         ('Permissions', {
#             'fields': ('is_active', 'is_superuser', 'groups', 'user_permissions'),
#         }),
#         ('Important dates', {'fields': ('last_login',)}),
#     )
 
#     list_display = ('email',)
#     list_filter = ('email', 'first_name', 'last_name',)
#     search_fields = ('email', 'first_name', 'last_name',)
#     filter_horizontal = ()
#     ordering = ('email',)
#     add_fieldsets = (
#         ("User Details", {'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'date_of_birth')}),
#     )
# admin.site.register(models.CustomUser, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """Регистрация модели CustomUser в админ панели"""

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
 
    list_display = ('email',)
    list_filter = ('email', 'first_name', 'last_name',)
    search_fields = ('email', 'first_name', 'last_name',)
    filter_horizontal = ()
    ordering = ('email',)
    add_fieldsets = (
        ("User Details", {'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'phone_number', 'date_of_birth')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
