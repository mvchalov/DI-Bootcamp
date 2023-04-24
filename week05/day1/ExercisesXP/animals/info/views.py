from django.shortcuts import render
from django.forms.models import model_to_dict
from .models import Animal, Family


# Create your views here.
def index(request):
    context = {
        "title": "Animals",
        "families": Family.objects.all(),
        "animals": Animal.objects.all(),
        "template_part": "inner_index.html"
    }
    return render(request, 'index.html', context)


def family(request, family_id):
    context = {
        "title": Family.objects.get(id=family_id).name+" Family",
        "animal_family": Family.objects.get(id=family_id).name+" Family",
        "animals": Animal.objects.filter(family__id=family_id),
        "template_part": "inner_family.html"
    }
    return render(request, 'index.html', context)


def animal(request, animal_id):
    current_animal = Animal.objects.get(id=animal_id)
    context = {
        "title": current_animal.name,
        "animal": model_to_dict(current_animal),
        "family": current_animal.family,
        "template_part": "inner_animal.html"
    }
    return render(request, 'index.html', context)


def families(request):
    context = {
        "title": "Families",
        "families": Family.objects.all(),
        "template_part": "inner_families.html"
    }
    return render(request, 'index.html', context)


def animals(request):
    context = {
        "title": "Animals",
        "animals": Animal.objects.all(),
        "template_part": "inner_animals.html"
    }
    return render(request, 'index.html', context)