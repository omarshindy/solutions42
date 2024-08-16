from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from wagtail.models import Page, Orderable, Locale
from wagtail.snippets.models import register_snippet
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel, PageChooserPanel, InlinePanel

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from .blocks import VisionBlock, NewsBlock, ImageSliderBlock



@register_snippet
class NavbarItem(Orderable):
    navbar = ParentalKey('Navbar', related_name='items', on_delete=models.CASCADE)
    page = models.ForeignKey(Page, null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        PageChooserPanel('page'),
    ]

    def __str__(self):
        return self.page.title if self.page else "No Page Selected"

@register_snippet
class Navbar(ClusterableModel):
    POSITION_CHOICES = [
        ('header', 'Header'),
        ('footer', 'Footer'),
    ]
    
    title = models.CharField(max_length=255)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    
    panels = [
        FieldPanel('title'),
        FieldPanel('position'),
        InlinePanel('items', label="Navbar Items"),
    ]
    
    def __str__(self):
        return self.title


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

        # Get the current locale
        current_locale = Locale.get_active()

        # Filter NewsPage objects by the current locale and order by date
        all_news = NewsPage.objects.filter(locale=current_locale).live().order_by('-date')

        paginator = Paginator(all_news, 5)

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