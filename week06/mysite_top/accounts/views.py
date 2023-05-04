from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .forms import ProfileForm

class ProfileView(DetailView):
    model = UserProfile
    template_name = 'profile.html'
    context_object_name = 'profile'

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def profile_redirect_view(request):

    user = request.user
    if hasattr(user, 'profile'):
        return redirect('update-profile', user.profile.id)
    
def update_profile(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        filled_form = ProfileForm(request.POST, instance=profile) # instance - the instance in the database to update
        if filled_form.is_valid():
            filled_form.save()
            return redirect('posts-all')
        else:
            errors = filled_form.errors
            print(errors)

    form = ProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'profile_update.html', context)

# class UpdateProfileView(UpdateView):

#     template_name = 'profile_update.html'
#     context_object_name = 'profile'
    
#     def post(self, request, *args, **kwargs): 
#         profile = self.get_object()
#         form = self.get_form()

#         if form.is_valid():
#             form.save()
#             return redirect('posts-all')
        