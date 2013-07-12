from django.views.generic import DetailView
from .models import AppCategory


class AppCategoryDetailView(DetailView):
    queryset = AppCategory.objects.all()
    context_object_name = "appcategory"