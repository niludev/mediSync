from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
    model = User
    # UserCreationForm and UserChangeForm automatically use set_password()
    add_form = UserCreationForm  # form used to create new users
    form = UserChangeForm  # form used to update existing users
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'role')
    list_filter = ('is_staff', 'is_active', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'phone_number')}),
        ('Address', {'fields': ('street', 'postal_code', 'city', 'state', 'country')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Other', {'fields': ('role',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'role', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)

# That is, register the User model with the UserAdmin settings in the admin panel.
admin.site.register(User, UserAdmin)
