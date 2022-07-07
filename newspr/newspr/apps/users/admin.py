from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

#Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {
            'fields': (
                'username', 'password', 'email',
                'first_name','last_name','image',
                'is_superuser','is_staff','is_active',
                'date_joined',
                )
        }),
        
    )

admin.site.register(CustomUser,CustomUserAdmin)


