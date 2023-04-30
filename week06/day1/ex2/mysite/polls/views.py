from django.shortcuts import render
from django.urls import reverse_lazy
from datetime import date
from django.views import generic
from .forms import PostForm
from .models import Post


# CRUD — Create — Retrieve — Update — Delete
class PostCreateView(generic.CreateView):
    template_name = 'create_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts_all')


class PostUpdateView(generic.UpdateView):
    template_name = 'create_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts_all')


class PostListView(generic.ListView):
    template_name = 'post_list.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_date'] = date.today()
        # post = self.get_object()
        return context


class PostView(generic.DetailView):
    template_name = 'post.html'
    model = Post
    context_object_name = 'post'
