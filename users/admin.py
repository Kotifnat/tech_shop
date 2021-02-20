from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ('date_joined',)
    list_display = ('email', 'username', 'date_joined', 'last_login',)


admin.site.register(CustomUser, CustomUserAdmin)
