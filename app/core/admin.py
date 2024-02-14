"""
Django Admin customization
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    """define the admin page for users"""
    ordering = ('id',)
    list_display = ('email', 'name')


admin.site.register(models.User, UserAdmin)
