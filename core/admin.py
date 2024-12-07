from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Solution

# Customizing User Admin to include mobile_number in the list display and form
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'mobile_number', 'is_staff', 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'mobile_number']
    ordering = ['username']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'mobile_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2')}),
        ('Personal info', {'fields': ('mobile_number',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )

# Customizing Solution Admin to make the solution-related fields more manageable
class SolutionAdmin(admin.ModelAdmin):
    list_display = ['solution_type', 'user', 'description', 'amount_to_charge', 'amount_willing_to_pay', 'created_at']
    search_fields = ['user__username', 'description', 'solution_type']
    list_filter = ['solution_type', 'created_at']
    ordering = ['-created_at']
    fields = ['user', 'solution_type', 'description', 'terms', 'created_at', 'amount_to_charge', 'amount_willing_to_pay']
    readonly_fields = ['created_at']

    def save_model(self, request, obj, form, change):
       
        super().save_model(request, obj, form, change)

# Register the custom admin classes
admin.site.register(User, CustomUserAdmin)
admin.site.register(Solution, SolutionAdmin)
