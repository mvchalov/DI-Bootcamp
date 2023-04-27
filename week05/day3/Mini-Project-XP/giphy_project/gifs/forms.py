from django import forms
from .models import Gif, Category

class GifForm(forms.ModelForm):
    class Meta:
        model = Gif
        fields = ('title', 'url', 'uploader_name')


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'