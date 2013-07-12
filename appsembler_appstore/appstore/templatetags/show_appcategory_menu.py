from django import template
from ..models import AppCategory

register = template.Library()


@register.inclusion_tag('appstore/includes/_appcategory_menu.html')
def show_appcategory_menu():
    categories = AppCategory.objects.all()
    return {'categories': categories}
