from django.shortcuts import render
from .forms import GifForm, CategoryForm
from .models import Gif, Category


# Create your views here.
def add_gif_view(request):

    if request.method == 'GET':
        gif_form = GifForm()
        context = {'form': gif_form}

    if request.method == 'POST':
        gif_filled_form = GifForm(request.POST)
        if gif_filled_form.is_valid():
            gif_filled_form.save()
        context = {'form': gif_filled_form}

    return render(request, 'add_gif.html', context)