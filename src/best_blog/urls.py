from django.urls import path
from .views import APIAuthor

urlpatterns = [
    path('authors/', APIAuthor.as_view()),
    path('authors/<int:pk>/', APIAuthor.as_view())
]
