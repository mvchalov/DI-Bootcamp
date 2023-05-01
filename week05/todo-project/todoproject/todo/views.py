from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Category, ToDo
from .forms import AddToDoForm, AddToCategoryForm
from datetime import date


# Create your views here.
class AddToDoView(generic.CreateView):
    template_name = 'add.html'
    model = ToDo
    form_class = AddToDoForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instance'] = 'Task'
        return context


class AddCategoryView(generic.CreateView):
    template_name = 'add.html'
    model = Category
    form_class = AddToCategoryForm
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instance'] = 'Category'
        return context


class ToDoListView(generic.ListView):
    template_name = 'todo_list.html'
    context_object_name = 'todos'
    model = ToDo

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_date'] = date.today()
        return context
