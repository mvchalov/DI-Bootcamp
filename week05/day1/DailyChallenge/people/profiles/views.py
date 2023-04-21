from django.shortcuts import render
from .models import get_people, get_person

# Create your views here.
def index(request):
    context = {
    }
    return render(request, 'index.html', context)


def people(request):
    context = {
        "people":  get_people()
    }
    return render(request, 'people.html', context)


def person(request, person_id):
    context = {
        "person_id": person_id,
        "person": get_person(person_id)
    }
    return render(request, 'person.html', context)
