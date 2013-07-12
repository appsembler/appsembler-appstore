from django.contrib import admin
from categories.admin import CategoryBaseAdmin
from .models import AppCategory, Application


class AppCategoryAdmin(CategoryBaseAdmin):
    pass


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'license_type', 'website')
    list_filter = ('category', 'license_type')


admin.site.register(Application, ApplicationAdmin)
admin.site.register(AppCategory, AppCategoryAdmin)
