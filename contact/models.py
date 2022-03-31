from django.db import models

from wagtail.core.blocks import StructBlock, CharBlock, TextBlock
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel


class TitleAndTextBlock(StructBlock):
    title = CharBlock(required=True, help_text="Add your title")
    text = TextBlock(required=True, help_text="Add additional text")

    class Meta:  # noqa
        template = "contact/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class ContactPage(Page):
    template = "contact/contact_page.html"

    content = StreamField(
        [
            ("title_and_text", TitleAndTextBlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = "Contact Page"
        verbose_name_plural = "Contact Pages"
