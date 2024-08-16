from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class ImageSliderBlock(blocks.StructBlock):
    images = blocks.ListBlock(
        ImageChooserBlock(),
        label="Slider Images"
    )

    class Meta:
        icon = "image"
        label = "Image Slider"
        template = "blocks/image_slider_block.html"
        translatable = True


class VisionBlock(blocks.StructBlock):
    title = blocks.TextBlock(label="Vision Title")
    image = ImageChooserBlock(label="Vision Image")

    class Meta:
        icon = "doc-full"
        label = "Vision Section"
        template = "blocks/vision_block.html"
        translatable = True


class LatestNewsBlock(blocks.StaticBlock):
    class Meta:
        icon = "placeholder"
        label = "Latest News"
        translatable = True
        # template = "blocks/news_block.html"

class NewsBlock(blocks.StructBlock):
    news = blocks.PageChooserBlock(required=True, target_model="home.NewsIndexPage")

    def get_context(self, value, parent_context=None):
        from .models import NewsPage

        context = super().get_context(value, parent_context=parent_context)
        news_page = value['news']

        latest_news = NewsPage.objects.child_of(news_page).live().order_by('-date')[:5]
        context['latest_news'] = latest_news
        context['news_section_title'] = news_page.title
        return context

    class Meta:
        template = "blocks/news_block.html"
        translatable = True