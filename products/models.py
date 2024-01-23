from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=1)
    image = models.ImageField(upload_to='images/', null=True, blank=True)


    def __str__(self):
        return self.title


class Animal(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=1)
    breed = models.CharField(max_length=100)


    def __str__(self):
        return self.name