# Generated by Django 5.0 on 2024-01-18 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0005_alter_women_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
