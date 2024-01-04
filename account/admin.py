from django.contrib import admin
from .models import Custom_User
from django.db.models import Case, When

# Register your models here.
@admin.register(Custom_User)
class Custom_User_Admin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'email', 'user_type', 'date_joined']
    list_filter = ['id', 'user_type', 'date_joined']
    search_fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type']
    ordering = (
        Case(
            When(user_type='Regular Users', then=1),
            When(user_type='Employee', then=2),
            When(user_type='Admin', then=3),
            default=4
        ),
    )

