import logging
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.cache import cache
from django.core.cache.utils import make_template_fragment_key
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from wagtailtrans.models import TranslatablePage, Language
from wagtail.core.models import Orderable, Page
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    StreamFieldPanel,
    ObjectList,
    TabbedInterface,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from ictcg.guidelines.choices import COLOUR_CHOICES
from ictcg.streams import blocks


class CacheClearMixin:

    def clear_from_caches(self):
        raise NotImplementedError("clear_from_caches function is required for subclasses")

    def save(self,  *args, **kwargs):
        self.clear_from_caches()
        return super().save(*args, **kwargs)


class GuidelinesListingPage(CacheClearMixin, TranslatablePage):
    """
    A TranslatablePage class used for the entry to the guidelines section of the site.
    The page lists the sections (GuidelinesSectionPages) within the guidelines.
    """

    parent_page_types = ["base.HomePage"]
    subpage_types = ["guidelines.GuidelinesSectionPage"]

    introduction = RichTextField(blank=True, default="")

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('introduction'),
    ]

    def clear_from_caches(self):
        target = "guidelines_footer"
        try:
            language_code = self.language.code
            target = make_template_fragment_key(target, [language_code])
            cache.delete(target)
        except Exception:
            logging.warning('Error deleting %s cache', target)


class GuidelinesSectionPage(CacheClearMixin, TranslatablePage):
    """
    A TranslatablePage class used for each section with the guidelines.
    The page lists the pages (GuidancePages) within the section.
    """

    parent_page_types = ["guidelines.GuidelinesListingPage"]
    subpage_types = ["guidelines.GuidancePage"]

    introduction = RichTextField(blank=True, default="")

    subtitle = models.CharField(
        max_length=140,
        blank=False
    )

    body = RichTextField(blank=True, default="")

    section_colour = models.CharField(
        max_length=140,
        choices=COLOUR_CHOICES,
        null=False,
        blank=False
    )

    landing_page_summary = models.CharField(
        max_length=240,
        null=True,
        blank=False,
        help_text=_("Text to be shown on the guidelines landing page")
    )

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
        FieldPanel("subtitle"),
        FieldPanel("body"),
        FieldPanel("section_colour"),
        FieldPanel("landing_page_summary"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('introduction'),
        index.SearchField('body'),
    ]

    def clear_from_caches(self):
        target = "sections_and_pages_for_listing"
        try:
            listing_id = self.get_parent().id
            target = make_template_fragment_key(target, [listing_id])
            cache.delete(target)
        except Exception:
            logging.warning('Error deleting %s cache', target)

        target = "pages_for_section"
        try:
            target = make_template_fragment_key(target, [self.id])
            cache.delete(target)
        except Exception:
            logging.warning('Error deleting %s cache', target)


# TODO: Hide snippets for other languages
# class CustomizedChooserPanel(SnippetChooserPanel):
#   def on_form_bound(self):
#     page_language = self.form.initial['language']
#     language_code = Language.objects.get(id=page_language)
#     choices = MoreInformationModule.objects.filter(language=language_code.code)
#     self.form.fields["more_information_module"].queryset = choices
#     super().on_form_bound()


class GuidancePage(CacheClearMixin, TranslatablePage):
    """
    A TranslatablePage class used for content pages (GuidancePages) within each guidelines section
    (GuidelinesSectionPages)
    """

    parent_page_types = ["guidelines.GuidelinesSectionPage"]
    subpage_types = []

    introduction = RichTextField(blank=True, default="")

    body = StreamField([
        ("content_section", blocks.RichTextWithTitleBlock()),
        ("dos_and_donts", blocks.DosAndDontsBlock()),
    ], null=True, blank=True)

    content_panels = TranslatablePage.content_panels + [
        FieldPanel("introduction"),
        StreamFieldPanel("body"),
    ]

    more_information_module = models.ForeignKey(
        'modules.MoreInformationModule',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    links_module = models.ForeignKey(
        'modules.LinksModule',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    Sidebar_panels = [
        SnippetChooserPanel("more_information_module"),
        SnippetChooserPanel("links_module")
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Sidebar_panels, heading='Sidebar'),
        ObjectList(TranslatablePage.settings_panels, heading='Settings'),
        ObjectList(TranslatablePage.promote_panels, heading='Promote')
    ])

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def get_context(self, request, *args, **kwards):
        context = super().get_context(request, *args, **kwards)
        guidelines = self.get_parent().get_parent()
        section = self.get_parent()

        prev_page = self.get_prev_siblings().live().first()
        next_page = self.get_next_siblings().live().first()

        if prev_page == None:
            prev_page = section.specific
            prev_page.title = prev_page.subtitle

        if next_page == None:
            next_page = section.get_next_siblings().live().first()

        context['prev_page'] = prev_page
        context['next_page'] = next_page

        context['guidelines'] = guidelines
        context['section'] = section

        return context

    def clear_from_caches(self):
        target = "sections_and_pages_for_listing"
        try:
            listing_id = self.get_parent().get_parent().id
            target = make_template_fragment_key(target, [listing_id])
            cache.delete(target)
        except Exception:
            logging.warning('Error deleting %s cache', target)

        target = "pages_for_section"
        try:
            section_id = self.get_parent().id
            target = make_template_fragment_key(target, [section_id])
            cache.delete(target)
        except Exception:
            logging.warning('Error deleting %s cache', target)


@receiver(pre_delete, sender=GuidelinesListingPage)
@receiver(pre_delete, sender=GuidelinesSectionPage)
@receiver(pre_delete, sender=GuidancePage)
def clear_caches_on_delete(sender, instance, **kwargs):
    instance.clear_from_caches()
