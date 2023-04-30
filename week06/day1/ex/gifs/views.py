from django.shortcuts import render
from .forms import CategoryForm, GifForm, LikeForm
from .models import Category, Gif
from django.http import HttpResponse

# Add new GIF view
def add_gif_view(request):

    if request.method == 'POST':

        gif_filled_form = GifForm(request.POST) # put the data from the request into the ModelForm

        if gif_filled_form.is_valid(): # check if all fields contain the correct data
            new_gif = gif_filled_form.save() # save data into database
            categories = gif_filled_form.cleaned_data['categories'] # <QuerySet [<Category: animals>]>

            new_gif.categories.add(*categories)  # [<Category: animals>, <Category: funny>]

            print("CATEGORY:", categories)
            return HttpResponse("SUCCESSFULLY SAVED")
        
        else:
            print(gif_filled_form.errors)
            return HttpResponse(gif_filled_form.errors)

    # GET mode - getting content out
    if request.method == 'GET':
        gif_form = GifForm()
        print("GET data: ", request.GET) # data associated with the GET method
        print("GETTING DATA OUT")
        context = {'form': gif_form}
        return render(request, 'gifs/add_gif.html', context)

# Add new Category view 

def add_category_view(request):

    if request.method == 'POST':
        print("POST data: ", request.POST)
        print('POSTING DATA')
        category_filled_form = CategoryForm(request.POST) # put the data from the request into the ModelForm

        if category_filled_form.is_valid(): # check if all fields contain the correct data
            category_filled_form.save() # save data into database
            return HttpResponse("SUCCESSFULLY SAVED")

    # GET mode - getting content out
    if request.method == 'GET':
        category_form = CategoryForm()
        print("GET data: ", request.GET) # data associated with the GET method
        print("GETTING DATA OUT")
        context = {'form': category_form}

    return render(request, 'gifs/add_category.html', context)


def gifs_view(request): 

    if request.method == 'POST':
        likeform_submitted = LikeForm(request.POST)
        if likeform_submitted.is_valid():

            gif = likeform_submitted.cleaned_data['gif']
            like = likeform_submitted.cleaned_data['like']

            if like:
                gif.likes += 1
            else:
                gif.likes -= 1
            
            gif.save()


    gifs_all = Gif.objects.all().order_by('title', 'likes')

    like_forms = [LikeForm(initial={'gif':gif_intsance, 'like': True}) for gif_intsance in gifs_all]
    dislike_forms = [LikeForm(initial={'gif':gif_intsance, 'like': False}) for gif_intsance in gifs_all]

    gifs_forms = list(zip(gifs_all, like_forms, dislike_forms))

    context = {'gifs_forms': gifs_forms}

    return render(request, 'gifs/gifs_all.html', context)
