from django.db import models


# Create your models here.
TYPE_CHOICES = (
    ('su', 'Sunny'),
    ('cl', 'Cloudy'),
    ('wi', 'Windy'),
    ('ra', 'Rainy'),
    ('st', 'Stormy'),
)


class Report(models.Model):
    location = models.CharField(max_length=100, default='')
    temperature = models.FloatField(default=-273)
    created_at = models.DateField(auto_now=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='su')


    def __str__(self):
        return f'{self.location}: {self.temperature} deg. C ({self.type})'


class Reporter(models.Model):
    pass