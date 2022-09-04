from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('update_task/<str:pk>/', views.UpdateTask, name='update_task'),
    path('delete/<str:pk>/', views.DeleteTask, name='delete'),
]