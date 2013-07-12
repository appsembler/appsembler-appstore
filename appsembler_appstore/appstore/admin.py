from django.contrib import admin
from categories.admin import CategoryBaseAdmin
from .models import AppCategory, Application


class AppCategoryAdmin(CategoryBaseAdmin):
    pass


admin.site.register(Application)
admin.site.register(AppCategory, AppCategoryAdmin)
