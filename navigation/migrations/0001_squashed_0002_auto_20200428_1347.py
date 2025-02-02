# Generated by Django 3.0.5 on 2020-04-28 13:54

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0045_assign_unlock_grouppagepermission"),
        ("wagtailimages", "0001_squashed_0021"),
    ]

    operations = [
        migrations.CreateModel(
            name="MainMenu",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                (
                    "language",
                    models.CharField(
                        choices=[("en", "English"), ("es", "LA Spanish"), ("id", "Bahasa")], max_length=100
                    ),
                ),
                (
                    "logo",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                    ),
                ),
                ("admin_title", models.CharField(max_length=100, null=True)),
                (
                    "button_aria_label",
                    models.CharField(
                        default="Show or hide Top Level Navigation",
                        help_text="Description for navigation button aria label",
                        max_length=100,
                    ),
                ),
                ("button_text", models.CharField(default="Menu", max_length=100)),
                (
                    "navigation_aria_label",
                    models.CharField(
                        default="Top Level Navigation",
                        help_text="Description for navigation aria label",
                        max_length=100,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MenuItem",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("sort_order", models.IntegerField(blank=True, editable=False, null=True)),
                ("title", models.CharField(blank=True, max_length=100)),
                ("url", models.CharField(blank=True, max_length=500)),
                ("open_in_new_tab", models.BooleanField(blank=True, default=False)),
                (
                    "menu",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="menu_items",
                        to="navigation.MainMenu",
                    ),
                ),
                (
                    "page",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailcore.Page",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
