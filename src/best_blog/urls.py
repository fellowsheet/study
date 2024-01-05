from django.urls import path
from .views import APIAuthor

urlpatterns = [
    path('authors/', APIAuthor.as_view())
]
