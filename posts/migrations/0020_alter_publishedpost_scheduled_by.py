# Generated by Django 4.1 on 2022-08-27 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0019_alter_schedule_scheduled_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishedpost',
            name='scheduled_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
