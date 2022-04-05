import datetime
from django import template

from blog.models import BlogCategory


register = template.Library()


@register.simple_tag
def get_categories():
    return BlogCategory.objects.all()
