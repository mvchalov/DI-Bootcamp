from django import forms
from .models import Category, ToDo


class AddToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = '__all__'


class AddToCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
