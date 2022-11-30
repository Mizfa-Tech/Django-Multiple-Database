from django.contrib import admin
from django.contrib.auth import get_user_model


@admin.register(get_user_model())
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_superuser', 'is_staff')
