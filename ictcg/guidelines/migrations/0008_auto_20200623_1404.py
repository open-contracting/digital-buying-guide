# Generated by Django 3.0.5 on 2020-06-23 14:04

import wagtail.core.blocks
import wagtail.core.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("guidelines", "0007_auto_20200612_1249"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guidancepage",
            name="body",
            field=wagtail.core.fields.StreamField(
                [
                    (
                        "content_section",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(
                                        help_text="Section title, max length 120 characters", max_length=120
                                    ),
                                ),
                                ("content", wagtail.core.blocks.RichTextBlock()),
                            ]
                        ),
                    ),
                    (
                        "dos_and_donts",
                        wagtail.core.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.core.blocks.CharBlock(help_text="Do's and dont's title", max_length=200),
                                ),
                                (
                                    "dos",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "item",
                                                    wagtail.core.blocks.CharBlock(
                                                        help_text="Item text", max_length=250
                                                    ),
                                                )
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "donts",
                                    wagtail.core.blocks.ListBlock(
                                        wagtail.core.blocks.StructBlock(
                                            [
                                                (
                                                    "item",
                                                    wagtail.core.blocks.CharBlock(
                                                        help_text="Item text", max_length=250
                                                    ),
                                                )
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
            ),
        ),
    ]
