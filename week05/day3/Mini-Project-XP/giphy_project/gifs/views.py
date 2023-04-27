from django.shortcuts import render
from .forms import GifForm, CategoryForm, LikeForm
from .models import Gif, Category
from django.http import HttpResponse


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


def gifs_with_likes(the_gifs):
    likes = [LikeForm(initial={'gif': item}) for item in the_gifs]
    return {'gifs': list(zip(the_gifs, likes))}


# Create your views here.
def add_gif_view(request):
    context = request_form(GifForm, request)
    return render(request, 'add_gif.html', context)


def add_category_view(request):
    context = request_form(CategoryForm, request)
    return render(request, 'add_gif.html', context)


def gifs(request):
    if request.method == 'POST':
        curr_item = Gif.objects.get(id=request.POST.get('form_id'))
        if request.POST.get('like'):
            curr_item.likes += 1
        if request.POST.get('dislike'):
            curr_item.likes -= 1
        curr_item.save()

    return render(request, 'gifs.html', gifs_with_likes(Gif.objects.all()))


def gifs_by_category(request, category):
    return render(request, 'gifs.html', gifs_with_likes(Category.objects.get(name=category.lower()).gifs.all()))


def categories(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'categories.html', context)


def liked_gifs(request):
    return render(request, 'gifs.html', gifs_with_likes(Gif.objects.filter(likes__gt=0).order_by('likes')))