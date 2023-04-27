from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Person(models.Model):
    # id is created automatically
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=100)


class Profile(models.Model):
    person = models.OneToOneField('Person', on_delete=models.CASCADE)
    country_origin = models.CharField(max_length=50)
    languages = models.ManyToManyField('Language')

    def __str__(self):
        return f"{self.country_origin}"


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"