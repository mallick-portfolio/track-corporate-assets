from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('id', 'first_name', 'last_name', 'email')
    list_filter = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password", 'first_name', 'last_name', 'phone', 'gender', 'user_type',)}),
        ("Permissions", {"fields": ('is_staff',  "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
               'first_name', 'last_name', 'phone', 'gender', 'user_type', "password1", "password2","is_staff",
                "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)