# Generated by Django 4.1 on 2023-10-27 19:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('economical_data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interestrate',
            name='time_scraped',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
