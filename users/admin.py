from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    readonly_fields = ('date_joined',)


admin.site.register(CustomUser, CustomUserAdmin)
