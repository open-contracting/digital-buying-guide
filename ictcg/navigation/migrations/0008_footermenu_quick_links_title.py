# Generated by Django 3.0.5 on 2020-07-23 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0007_auto_20200708_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='footermenu',
            name='quick_links_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]