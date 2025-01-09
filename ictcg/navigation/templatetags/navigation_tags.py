from django import template
from django.utils.translation import get_language
from wagtail.core.models import Page
from ictcg.navigation.models import MainMenu, FooterMenu
from ictcg.guidelines.models import GuidelinesListingPage
import urllib.parse

register = template.Library()


# Retrieves the ancestors of the current page,
# filtering out the top 2 levels (root and translation-root)
@register.inclusion_tag("includes/breadcrumbs.html", takes_context=True)
def breadcrumbs(context):
    self = context.get("self")
    if self is None or self.depth <= 2:
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(self, inclusive=True).filter(depth__gt=2)
    parent = get_parent(ancestors, self.depth)
    return {
        "ancestors": ancestors,
        "parent": parent,
        "request": context["request"],
    }


def get_parent(ancestors, child_depth):
    """Get the parent based on the depth of the current item"""
    for item in ancestors:
        if item.depth == (child_depth - 1):
            return item
    return None


@register.simple_tag()
def main_menu(language):
    mainmenu = MainMenu.objects.filter(language=language).first()
    if mainmenu:
        return mainmenu
    else:
        # Default to en if not set for the other countries
        return MainMenu.objects.filter(language="en").first()


@register.simple_tag(takes_context=True)
def is_main_menu_link_active(context, link):
    request = context.get("request")
    if request:
        return urllib.parse.unquote(link) in request.path
    return False


@register.simple_tag()
def get_footer_content():
    language = get_language()
    guildelines = GuidelinesListingPage.objects.filter(language__code=language).live()
    footer_content = FooterMenu.objects.filter(language=language).first()
    return {
        "guildelines": guildelines,
        "footer_content": footer_content,
    }
