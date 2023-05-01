from django.contrib import admin
from django.urls import path
from .views import AddToDoView, AddCategoryView, ToDoListView

urlpatterns = [
    path('add_todo/', AddToDoView.as_view(), name='add_todo'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('', ToDoListView.as_view(), name="home"),
]