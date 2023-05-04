from typing import Any, Dict, Type
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from datetime import date
from django.views import generic
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# from zoneinfo import ZoneInfo
# TIMEZONE = ZoneInfo("Asia/Jerusalem")

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
        today = date.today()
        # today.tz_info = TIMEZONE
        initial_data = {'author': profile,
                        'date_created': today}
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
        
        user = self.request.user
        if hasattr(user, 'profile'):
            author = self.request.user.profile
            posts = self.get_queryset()
            comments = [CommentForm(initial={'post': post, 'author': author}) for post in posts]
            context['posts_comments'] = zip(posts, comments)

        return context


def add_comment(request): 

    if request.method == 'POST':
        filled_form = CommentForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
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
    