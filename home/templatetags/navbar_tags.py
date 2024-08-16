from django import template
from django.utils.translation import get_language
from wagtail.models import Locale
from ..models import Navbar

register = template.Library()

@register.simple_tag(takes_context=True)
def get_navbars(context):
    current_language = get_language()

    try:
        # Get the locale corresponding to the current language
        current_locale = Locale.objects.get(language_code=current_language)
    except Locale.DoesNotExist:
        # Fallback to the default locale if the specific locale doesn't exist
        current_locale = Locale.get_default()

    navbars = Navbar.objects.all()

    # Create a list to hold the modified navbars
    localized_navbars = []

    for navbar in navbars:
        # Clone the navbar instance attributes
        localized_navbar = {
            'id': navbar.id,
            'title': navbar.title,
            'position': navbar.position,
            'items': []
        }

        for item in navbar.items.all():
            if item.page:
                # Attempt to get the translated page
                translated_page = item.page.get_translation_or_none(locale=current_locale)
                if translated_page:
                    item.page = translated_page
            localized_navbar['items'].append(item)

        localized_navbars.append(localized_navbar)

    return localized_navbars
