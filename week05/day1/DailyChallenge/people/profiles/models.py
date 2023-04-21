from django.db import models


class People(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    country = models.CharField(max_length=50)


# Create your models here.
def get_people():
    people = People.objects.order_by('-age')
    return people


def get_person(person_id):
    person = People.objects.get(id=person_id)
    return person
