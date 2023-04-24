from django.db import models


class Family(models.Model):
    # id is created automatically
    name = models.CharField(max_length=50)
    pic = models.CharField(max_length=100)
    description = models.TextField


class Animal(models.Model):
    name = models.CharField(max_length=50)
    legs = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    family = models.ForeignKey(Family, on_delete=models.SET_NULL, null=True)
    pic = models.CharField(max_length=100)


indata = None


# Create your models here.
def get_indata():
    with open('tmp-indata.json', 'r') as jss:
        global indata
        indata = json.loads("".join([e for e in jss]))


def get_animals_by_family(family):
    if indata is None:
        get_indata()
    results = []
    for item in indata['animals']:
        if item['family'] == family:
            results.append(item)
    return results


def get_family_by_id(family_id):
    if indata is None:
        get_indata()
    return list(filter(lambda e: e['id'] == family_id, indata['families']))[0]


def get_animal_by_id(animal_id):
    if indata is None:
        get_indata()
    return list(filter(lambda e: e['id'] == animal_id, indata['animals']))[0]


def get_families():
    if indata is None:
        get_indata()
    return indata['families']


def get_animals():
    if indata is None:
        get_indata()
    return indata['animals']
