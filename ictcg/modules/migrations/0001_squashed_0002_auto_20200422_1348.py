# Generated by Django 3.0.5 on 2020-04-22 15:16

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LinksModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('en', 'English'), ('es', 'LA Spanish'), ('id', 'Bahasa')], max_length=100)),
                ('admin_title', models.CharField(max_length=140, null=True)),
                ('title', models.CharField(max_length=140, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MoreInformationModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_text', models.CharField(blank=True, help_text='Title', max_length=140)),
                ('url', models.URLField(blank=True, null=True)),
                ('open_in_new_tab', models.BooleanField(blank=True, default=False)),
                ('language', models.CharField(choices=[('en', 'English'), ('es', 'LA Spanish'), ('id', 'Bahasa')], max_length=100)),
                ('admin_title', models.CharField(max_length=140, null=True)),
                ('title', models.CharField(max_length=140, null=True)),
                ('description', models.CharField(blank=True, max_length=140, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrderableLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_text', models.CharField(blank=True, help_text='Title', max_length=140)),
                ('url', models.URLField(blank=True, null=True)),
                ('open_in_new_tab', models.BooleanField(blank=True, default=False)),
                ('links', modelcluster.fields.ParentalKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='orderable_links', to='modules.LinksModule')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
