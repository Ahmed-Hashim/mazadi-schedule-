# Generated by Django 4.1 on 2022-08-23 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_schedule_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='published',
            field=models.BooleanField(default='False'),
        ),
    ]
