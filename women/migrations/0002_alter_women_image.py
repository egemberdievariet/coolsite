# Generated by Django 5.0 on 2023-12-20 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='image',
            field=models.ImageField(null=True, upload_to='women/'),
        ),
    ]
