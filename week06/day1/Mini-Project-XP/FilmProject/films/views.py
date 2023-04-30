from django.urls import reverse_lazy
from django.views import generic
from .forms import AddDirectorForm, AddFilmForm
from .models import Film, Director
from datetime import date


# Create your views here.
class AddFilmView(generic.CreateView):
    template_name = 'add_instance.html'
    model = Film
    form_class = AddFilmForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instance'] = "Film"
        return context


class EditFilmView(generic.UpdateView):
    template_name = 'add_instance.html'
    model = Film
    form_class = AddFilmForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instance'] = "Film"
        return context


class AddDirectorView(generic.CreateView):
    template_name = 'add_instance.html'
    model = Director
    form_class = AddDirectorForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instance'] = "Director"
        return context


class EditDirectorView(generic.UpdateView):
    template_name = 'add_instance.html'
    model = Director
    form_class = AddDirectorForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instance'] = "Director"
        return context


class HomepageView(generic.ListView):
    template_name = 'homepage.html'
    model = Film
    context_object_name = 'films'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_date'] = date.today()
        return context
