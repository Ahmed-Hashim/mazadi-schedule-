# Generated by Django 4.1 on 2022-08-23 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_schedule_publishedposts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PublishedPosts',
            new_name='PublishedPost',
        ),
    ]