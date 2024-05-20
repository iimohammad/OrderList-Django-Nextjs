from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('full_name','phone','is_verify_phone' ,'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('full_name','phone','is_verify_phone','password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2', 'is_staff', 'is_superuser')}
        ),
    )
    search_fields = ('phone',)
    ordering = ('phone',)

admin.site.register(User, CustomUserAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'state', 'city', 'address','date',)
    search_fields = ('user__phone', 'state', 'city')
    list_filter = ('gender', 'state', 'city')
    readonly_fields = ('date',)