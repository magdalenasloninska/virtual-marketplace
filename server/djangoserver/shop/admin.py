from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Listing


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ('username', 'email', 'is_staff', 'is_active')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('about', 'profile_picture')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
    )

    list_filter = ('is_staff', 'is_active')

    search_fields = ('username', 'email')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Listing)