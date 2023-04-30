"""
URL configuration for FilmProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from films.views import HomepageView, AddFilmView, AddDirectorView, EditFilmView, EditDirectorView

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', HomepageView.as_view(), name="home"),
    path('add_film/', AddFilmView.as_view(), name="add_film"),
    path('add_director/', AddDirectorView.as_view(), name="add_director"),
    path('edit_film/<int:pk>/', EditFilmView.as_view(), name="edit_film"),
    path('edit_director/<int:pk>/', EditDirectorView.as_view(), name="edit_director"),
]
