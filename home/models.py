from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel


from .blocks import VisionBlock, NewsBlock, ImageSliderBlock

class HomePage(Page):
    body = StreamField([
        ('image_slider', ImageSliderBlock()),
        ('vision_section', VisionBlock()),
        ('news_block', NewsBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]


class NewsPage(Page):
    date = models.DateField("Post date")
    body = RichTextField()
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body'),
        FieldPanel('image'),
    ]

    parent_page_types = ['NewsIndexPage']


class NewsIndexPage(Page):
    def get_context(self, request):
        context = super().get_context(request)
        all_news = NewsPage.objects.live().order_by('-date')
        paginator = Paginator(all_news, 1)

        page = request.GET.get("page")
        try:
            news = paginator.page(page)
        except PageNotAnInteger:
            news = paginator.page(1)
        except EmptyPage:
            news = paginator.page(paginator.num_pages)

        context['news'] = news
        return context

    subpage_types = ['NewsPage']