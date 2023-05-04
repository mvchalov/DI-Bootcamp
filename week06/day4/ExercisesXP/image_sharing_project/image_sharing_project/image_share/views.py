from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.views.generic import FormView
from django.urls import reverse_lazy
from .models import Profile, Image
from .forms import ImageUploadForm


# Create your views here.
class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, profile_owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = Image.objects.filter(image_owner=self.request.user)
        return context


class UploadImage(LoginRequiredMixin, FormView):
    form_class = ImageUploadForm
    template_name = 'image_share/upload.html'
    success_url = reverse_lazy('account_profile')

    def form_valid(self, form):
        form.instance.image_owner = self.request.user
        form.save()
        print("here", form)

        return super().form_valid(form)
