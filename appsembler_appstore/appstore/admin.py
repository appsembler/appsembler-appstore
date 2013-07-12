from django.contrib import admin
from categories.admin import CategoryBaseAdmin
from .models import AppCategory


class AppCategoryAdmin(CategoryBaseAdmin):
    pass


admin.site.register(AppCategory, AppCategoryAdmin)
