from django.shortcuts import render
from .models import Person


# Create your views here.
def find_profile(model, value):
    result = None
    try:
        model_instance = model.objects.get(name=value)
        result = model_instance
    except model.DoesNotExist:
        pass
    try:
        model_instance = model.objects.get(phone_number=value)
        result = model_instance
    except model.DoesNotExist:
        pass

    return result


def f_name(request, search_value: str):
    person_name = find_profile(Person, search_value)
    if person_name is not None:
        person_profile = person_name.profile
        profile_languages = ", ".join([*map(lambda e: e.name, [*person_profile.languages.all().order_by('name')])])
        context = {
            'person_info': person_name,
            'person_profile': person_profile,
            'languages': profile_languages
        }
    else:
        context = {}
    return render(request, 'name.html', context)