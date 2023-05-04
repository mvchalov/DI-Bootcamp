from typing import Any, Dict, Type
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from datetime import date
from django.views import generic
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# CRUD - CREATE - RETRIEVE - UPDATE - DELETE

@login_required(login_url=reverse_lazy('login'))
def a_view(request):
    ...


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    template_name = 'create_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("posts-all")

    def get_initial(self) -> Dict[str, Any]:
        user = self.request.user
        profile = user.profile
        initial_data = {'author': profile}
        return initial_data


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = reverse_lazy('login')
    template_name = 'update_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("posts-all")


class PostListView(generic.ListView):
    template_name = 'post_list.html'
    context_object_name = 'posts'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.get_queryset()
        user = self.request.user
        if hasattr(user, 'profile'):
            comments = [CommentForm(initial={'post': post, 'author': self.request.user.profile}) for post in posts]
            context['posts_comments'] = zip(posts, comments)
        print("USER:", self.request.user)
        return context


def add_comment(request):
    if request.method == 'POST':
        filled_form = CommentForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            print("Comment is added")
            return redirect('posts-all')


class PostView(generic.DetailView):
    template_name = 'post.html'
    context_object_name = 'post'
    model = Post

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all()
        return context
