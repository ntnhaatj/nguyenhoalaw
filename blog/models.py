from django.db import models
from django import forms

from taggit.models import TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalManyToManyField, ParentalKey
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(verbose_name="slug",
                            allow_unicode=True,
                            max_length=255,
                            help_text="A slug to identify post by category")
    description = models.TextField(blank=True)
    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
        FieldPanel("description")
    ]

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ("name", )

    def __str__(self):
        return self.name


class BlogIndexPage(Page):
    parent_page_types = ("home.HomePage", )
    max_count = 1

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = BlogPage.objects.live().public().order_by('-first_published_at')

        if request.GET.get('tag', None):
            tag = request.GET.get('tag')
            all_posts = all_posts.filter(tags__slug__in=[tag])

        if request.GET.get('category', None):
            category = request.GET.get('category')
            all_posts = all_posts.filter(categories__slug__in=[category])

        context["posts"] = all_posts
        context["categories"] = request.GET.get('category', None) \
            or [cat.name for cat in BlogCategory.objects.all()]
        return context


class BlogTags(TaggedItemBase):
    content_object = ParentalKey(
        'blog.BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )


class BlogPage(Page):
    parent_page_types = ("blog.BlogIndexPage", )

    date = models.DateField("Post date")
    intro = models.CharField(max_length=255, help_text="Blog post introduction, max length 255")
    body = RichTextField(blank=True)
    categories = ParentalManyToManyField("blog.BlogCategory")
    tags = ClusterTaggableManager(through=BlogTags, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple, heading="Categories"),
        FieldPanel("tags"),
    ]
