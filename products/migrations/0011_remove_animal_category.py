# Generated by Django 5.0 on 2024-01-08 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_product_category_animal_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='category',
        ),
    ]