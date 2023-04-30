from django.db import models
from datetime import date


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Director(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING, blank=True)
    film = models.ManyToManyField('Film', related_name='films', blank=True)

    def __str__(self):
        return f"{self.name}"


class Film(models.Model):
    title = models.CharField(max_length=50)
    release_date = models.DateTimeField(default=date.today())
    created_in_country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    available_in_countries = models.ManyToManyField(Country, related_name='countries', blank=True)
    category = models.ManyToManyField(Category, related_name='categories', blank=True)
    director = models.ManyToManyField(Director, related_name='directors', blank=True)

    def __str__(self):
        return f"{self.title} ({self.release_date.date()}, {self.created_in_country})"
