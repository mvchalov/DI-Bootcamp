from django.db import models
from datetime import date


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateTimeField(default=date.today())
    date_completion = models.DateTimeField(default=None, blank=True, null=True)
    date_deadline = models.DateTimeField(default=None, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.title} ({self.date_deadline})"


