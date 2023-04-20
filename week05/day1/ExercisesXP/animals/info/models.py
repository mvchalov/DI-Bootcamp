import json

from django.db import models

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
