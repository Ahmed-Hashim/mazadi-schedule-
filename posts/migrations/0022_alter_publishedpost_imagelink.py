# Generated by Django 4.1 on 2022-08-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0021_schedule_design_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publishedpost',
            name='imagelink',
            field=models.ImageField(blank=True, null=True, upload_to='images/designs/'),
        ),
    ]
