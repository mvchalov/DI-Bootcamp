from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (ProfileView,
                    SignUpView,
                    update_profile,
                    profile_redirect_view)

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile-page'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('update-profile/', update_profile, name='update-profile'),
    path('profile-redirect/', profile_redirect_view, name='profile-redirect')
]
