# Generated by Django 3.0.5 on 2020-05-21 13:17

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):
    dependencies = [
        ("navigation", "0003_auto_20200520_1526"),
    ]

    operations = [
        migrations.AddField(
            model_name="mainmenu",
            name="phase_banner_description",
            field=wagtail.core.fields.RichTextField(
                blank=True, default="", help_text="Text area for phase banner description"
            ),
        ),
    ]
