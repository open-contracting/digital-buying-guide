# Generated by Django 3.0.5 on 2020-05-05 11:30

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):
    dependencies = [
        ("wagtailimages", "0001_squashed_0021"),
        ("navigation", "0001_squashed_0002_auto_20200428_1347"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="menuitem",
            options={},
        ),
        migrations.RemoveField(
            model_name="menuitem",
            name="menu",
        ),
        migrations.RemoveField(
            model_name="menuitem",
            name="sort_order",
        ),
        migrations.CreateModel(
            name="MainMenuItem",
            fields=[
                (
                    "menuitem_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="navigation.MenuItem",
                    ),
                ),
                ("sort_order", models.IntegerField(blank=True, editable=False, null=True)),
                (
                    "links",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="menu_items",
                        to="navigation.MainMenu",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
            bases=("navigation.menuitem", models.Model),
        ),
        migrations.CreateModel(
            name="FooterMenu",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("admin_title", models.CharField(max_length=100, null=True)),
                (
                    "language",
                    models.CharField(
                        choices=[("en", "English"), ("es", "LA Spanish"), ("id", "Bahasa")], max_length=100
                    ),
                ),
                ("sponsors_title", models.CharField(max_length=100, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="FooterMenuItem",
            fields=[
                (
                    "menuitem_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="navigation.MenuItem",
                    ),
                ),
                ("sort_order", models.IntegerField(blank=True, editable=False, null=True)),
                (
                    "links",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="footer_menu_items",
                        to="navigation.FooterMenu",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
            bases=("navigation.menuitem", models.Model),
        ),
        migrations.CreateModel(
            name="SponsorItem",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("sort_order", models.IntegerField(blank=True, editable=False, null=True)),
                ("name", models.CharField(blank=True, help_text="Title", max_length=140)),
                ("url", models.URLField(blank=True, help_text="URL for sponsor link")),
                (
                    "logo",
                    models.ForeignKey(
                        help_text="Sponsor image or logo",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.Image",
                    ),
                ),
                (
                    "sponsor",
                    modelcluster.fields.ParentalKey(
                        default="",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sponsor_items",
                        to="navigation.FooterMenu",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
