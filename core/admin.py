from django.contrib import admin

from .models import User, Task

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "status", "due_data", "user")