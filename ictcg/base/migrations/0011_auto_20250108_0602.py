# Generated by Django 3.1.14 on 2025-01-08 06:02

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailforms", "0004_add_verbose_name_plural"),
        ("wagtailcore", "0059_apply_collection_ordering"),
        ("wagtailtrans", "0009_create_initial_language"),
        ("wagtailredirects", "0006_redirect_increase_max_length"),
        ("base", "0010_genericpage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "rich_text_section",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Section title, max length 120 characters",
                                        max_length=120,
                                        required=False,
                                    ),
                                ),
                                (
                                    "width",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("full", "Full Width"),
                                            ("half", "Half Width"),
                                            ("two-thirds", "Two Thirds"),
                                        ]
                                    ),
                                ),
                                (
                                    "text_alignment",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[("left", "Left"), ("centre", "Centred"), ("right", "Right")]
                                    ),
                                ),
                                ("content", wagtail.core.blocks.RichTextBlock(required=False)),
                            ]
                        ),
                    ),
                    (
                        "highlight_list_section",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Section title, max length 120 characters", max_length=120
                                    ),
                                ),
                                (
                                    "items_list",
                                    wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock(label="Item")),
                                ),
                            ]
                        ),
                    ),
                    (
                        "case_study_section",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Section title, max length 120 characters", max_length=120
                                    ),
                                ),
                                (
                                    "text_alignment",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[("left", "Left"), ("centre", "Centred"), ("right", "Right")]
                                    ),
                                ),
                                ("content", wagtail.core.blocks.RichTextBlock()),
                                (
                                    "button_text",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Text for button", max_length=120, required=False
                                    ),
                                ),
                                ("button_link", wagtail.core.blocks.PageChooserBlock()),
                            ]
                        ),
                    ),
                    (
                        "sponsors_section",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Section title, max length 120 characters",
                                        max_length=120,
                                        required=False,
                                    ),
                                ),
                                (
                                    "width",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[
                                            ("full", "Full Width"),
                                            ("half", "Half Width"),
                                            ("two-thirds", "Two Thirds"),
                                        ]
                                    ),
                                ),
                                (
                                    "text_alignment",
                                    wagtail.core.blocks.ChoiceBlock(
                                        choices=[("left", "Left"), ("centre", "Centred"), ("right", "Right")]
                                    ),
                                ),
                                ("content", wagtail.core.blocks.RichTextBlock(required=False)),
                            ],
                            template="streams/homepage_sponsors_block.html",
                        ),
                    ),
                ],
                blank=True,
                null=True,
            ),
        ),
        migrations.DeleteModel(
            name="CookiePage",
        ),
    ]
