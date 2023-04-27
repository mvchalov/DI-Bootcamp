from django.shortcuts import render
from .forms import GifForm, CategoryForm
from .models import Gif, Category


def request_form(form, request):
    if request.method == 'GET':
        curr_form = form()
        return {'form': curr_form}
    elif request.method == 'POST':
        curr_form = form(request.POST)
        if curr_form.is_valid():
            curr_form.save()
        return {'form': curr_form}
    else:
        return {}


# Create your views here.
def add_gif_view(request):
    context = request_form(GifForm, request)
    return render(request, 'add_gif.html', context)


def add_category_view(request):
    context = request_form(CategoryForm, request)
    return render(request, 'add_gif.html', context)


def gifs(request):
    context = {'gifs': Gif.objects.all()}
    return render(request, 'gifs.html', context)


def gifs_by_category(request, category):
    context = {'gifs': Category.objects.get(name=category.lower()).gifs.all()}
    return render(request, 'gifs.html', context)


def categories(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'categories.html', context)