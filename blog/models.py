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
    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ("name", )

    def __str__(self):
        return self.name


class BlogTags(TaggedItemBase):
    content_object = ParentalKey(
        'blog.BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )


class BlogIndexPage(Page):
    parent_page_types = ("home.HomePage", )
    max_count_per_parent = 1

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


class BlogPage(Page):
    parent_page_types = (BlogIndexPage, )

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
