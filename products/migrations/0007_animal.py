# Generated by Django 5.0 on 2024-01-07 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.ImageField(default=1, upload_to='')),
                ('breed', models.CharField(max_length=100)),
            ],
        ),
    ]
