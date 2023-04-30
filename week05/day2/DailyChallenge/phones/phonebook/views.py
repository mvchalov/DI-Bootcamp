from django.shortcuts import render, redirect, reverse
from .models import Person, Profile
from .forms import PersonForm


# Create your views here.
def find_profile(model, value):
    result = None
    try:
        return model.objects.get(name=value)
    except model.DoesNotExist:
        pass
    try:
        return model.objects.get(phone_number=value)
    except model.DoesNotExist:
        pass

    return result


def f_name(request, search_value: str):
    context = {}
    person_name = find_profile(Person, search_value)
    if person_name is not None:
        if hasattr(person_name, 'profile'):
            person_profile = person_name.profile
            profile_languages = ", ".join([*map(lambda e: e.name, [*person_profile.languages.all().order_by('name')])])
            context = {
                'person_info': person_name,
                'person_profile': person_profile,
                'languages': profile_languages
            }
        else:
            context = {'person_info': person_name}
    return render(request, 'name.html', context)


def request_form(form, request):
    if request.method == 'GET':
        curr_form = form()
        return {'form': curr_form}
    elif request.method == 'POST':
        curr_form = form(request.POST)
        print(curr_form.is_valid())
        if curr_form.is_valid():
            new_item = curr_form.save()
            new_profile = Profile()
            new_profile.person = new_item
            new_profile.save()
            search_name = new_item.name
            print(search_name)
            return redirect('phonebook:f_name', search_value=search_name)
    else:
        return {}


def add_person(request):
    context = request_form(PersonForm, request)
    return render(request, 'add_person.html', context)
