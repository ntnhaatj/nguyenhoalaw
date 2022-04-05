import datetime
from django import template

from blog.models import BlogCategory, BlogPage


register = template.Library()


@register.simple_tag
def get_categories():
    return BlogCategory.objects.all()


@register.simple_tag
def get_latest_blog_posts():
    posts = BlogPage.objects.live().public().order_by("-first_published_at")
    return posts


@register.simple_tag
def get_latest_blog_posts_by_category(category):
    posts = BlogPage.objects.live()\
        .public()\
        .filter(categories__contains=[category])\
        .order_by("-first_published_at")
    return posts
