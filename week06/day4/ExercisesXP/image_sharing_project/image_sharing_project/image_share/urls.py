from django.contrib import admin
from django.urls import path, include
from .views import ProfileView, UploadImage

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', ProfileView.as_view(), name='account_profile'),
    path('upload/', UploadImage.as_view())
]