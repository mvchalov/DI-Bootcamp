views.py: 
```py
def gifs_view(request): 

    if request.method == 'POST':

        like_dislike_form = LikeForm(request.POST)
        if like_dislike_form.is_valid():
            gif_instance = like_dislike_form.cleaned_data['gif']
            like_val = like_dislike_form.cleaned_data['like']
            print(like_val)
            if like_val:
                gif_instance.likes += 1
            else:
                gif_instance.likes -= 1

            gif_instance.save()
            
            return redirect('gifs')

    gifs_all = Gif.objects.all()
    like_forms = [LikeForm(initial={'gif':gif_intsance, 'like': True}) for gif_intsance in gifs_all]
    dislike_forms = [LikeForm(initial={'gif':gif_intsance, 'like': False}) for gif_intsance in gifs_all]

    gifs_forms = list(zip(gifs_all, like_forms, dislike_forms))

    context = {'gifs_forms': gifs_forms}

    return render(request, 'gifs/gifs_all.html', context)
```

forms.py:
```py
from django import forms 
from .models import Gif, Category

class GifForm(forms.ModelForm):

    class Meta: 
        model = Gif
        fields = ('title', 'url', 'uploader_name')
        exclude = ('likes',)
        widgets = {
            'title': forms.Textarea(attrs={'class': 'title-class', 'id': '1'})
        }

    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())
    

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.Textarea(attrs={'class': 'my_textarea'})
        }


class LikeForm(forms.Form):
    
    gif = forms.ModelChoiceField(queryset=Gif.objects.all(), widget=forms.HiddenInput())
    like = forms.BooleanField(widget=forms.HiddenInput())

```

models.py:
```py
from django.db import models


class Gif(models.Model):

    title = models.CharField(max_length=50)
    url = models.URLField()
    uploader_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True) 
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}, {self.uploader_name}'
    
class Category(models.Model):

    name = models.CharField(max_length=50)
    gifs = models.ManyToManyField(Gif, related_name='categories', blank=True)

    def __str__(self) -> str:
        return f'{self.name}'
```

gifs_all.html:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gifs</title>
</head>
<body>

    {%for gif, like, dislike in gifs_forms%}

        <br>
        
        {{gif}}

        {{gif.likes}}
        <br>
        <form method="POST">
            {%csrf_token%}
            {{like}}
            <button type="submit"> LIKE </button>
        </form>
        <br>
        <form method="POST">
            {%csrf_token%}
            {{dislike}}
            <button type="submit"> DISLIKE </button>
        </form>  

        <br>  
    {%endfor%}
    
</body>
</html>
```

Why when I'm clicking 'DISLIKE' nothing happens while clicking 'LIKE' increments the likes field of the Gif instance? 