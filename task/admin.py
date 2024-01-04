from django.contrib import admin
from .models import Task, Task_Photo
from django.db.models import Case, IntegerField, When

# Register your models here.
class Task_Photo_Inline(admin.TabularInline):
    model = Task_Photo

class Task_Admin(admin.ModelAdmin):
    inlines = [
        Task_Photo_Inline,
    ]
    list_display = ['title', 'due_date', 'priority', 'is_complete', 'created_date']
    list_filter = ['due_date', 'priority', 'is_complete', 'created_date']
    search_fields = ['title']
    ordering = (Case(
            When(priority='High', then=1),
            When(priority='Medium', then=2),
            When(priority='Low', then=3),
            default=4,
            output_field=IntegerField()
        ),)

admin.site.register(Task_Photo)
admin.site.register(Task, Task_Admin)

