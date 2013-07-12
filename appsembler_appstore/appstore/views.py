from django.views.generic import DetailView
from .models import AppCategory, Application


class AppCategoryDetailView(DetailView):
    queryset = AppCategory.objects.all()
    context_object_name = "appcategory"


class ApplicationDetailView(DetailView):
    queryset = Application.objects.all()
    context_object_name = "application"
