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
    location = models.CharField(max_length=100, null=False, blank=False),
    temperature = models.FloatField(default=-273, null=False, blank=False),
    created_at = models.DateTimeField(),
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, default='su')
