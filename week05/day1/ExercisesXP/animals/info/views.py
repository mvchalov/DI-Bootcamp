from django.shortcuts import render
from .models import get_animals_by_family, get_animal_by_id, get_family_by_id, get_families, get_animals


# Create your views here.
def index(request):
    context = {
        "title": "Animals",
        "families": get_families(),
        "animals": get_animals(),
    }
    return render(request, 'index.html', context)


def family(request, family_id):
    context = {
        "animal_family": get_family_by_id(family_id)['name'],
        "animals": get_animals_by_family(family_id)
    }
    return render(request, 'family.html', context)


def animal(request, animal_id):
    context = {
        "animal_name": get_animal_by_id(animal_id)['name'],
        "animals": get_animal_by_id(animal_id)
    }
    return render(request, 'animal.html', context)