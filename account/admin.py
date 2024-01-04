from django.contrib import admin
from .models import Custom_User

# Register your models here.
@admin.register(Custom_User)
class Custom_User_Admin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'email', 'user_type', 'date_joined']
    list_filter = ['id', 'user_type', 'date_joined']
    search_fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'user_type']

