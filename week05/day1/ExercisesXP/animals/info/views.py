from django.shortcuts import render
from .models import get_animals_by_family, get_animal_by_id, get_family_by_id, get_families, get_animals


# Create your views here.
def index(request):
    context = {
        "title": "Animals",
        "families": get_families(),
        "animals": get_animals(),
        "template_part": "inner_index.html"
    }
    return render(request, 'index.html', context)


def family(request, family_id):
    context = {
        "title": get_family_by_id(family_id)['name']+" Family",
        "animal_family": get_family_by_id(family_id)['name']+" Family",
        "animals": get_animals_by_family(family_id),
        "template_part": "inner_family.html"
    }
    return render(request, 'index.html', context)


def animal(request, animal_id):
    context = {
        "title": get_animal_by_id(animal_id)['name'],
        "animal_name": get_animal_by_id(animal_id)['name'],
        "animals": get_animal_by_id(animal_id),
        "family": get_family_by_id(get_animal_by_id(animal_id)['family']),
        "template_part": "inner_animal.html"
    }
    return render(request, 'index.html', context)


def families(request):
    context = {
        "title": "Families",
        "families": get_families(),
        "template_part": "inner_families.html"
    }
    return render(request, 'index.html', context)


def animals(request):
    context = {
        "title": "Animals",
        "animals": get_animals(),
        "template_part": "inner_animals.html"
    }
    return render(request, 'index.html', context)