from django.urls import path
from .views import AuthorListGeneric, AuthorDetailGeneric, \
    PostListGeneric, PostDetailGeneric

urlpatterns = [
    path('authors/', AuthorListGeneric.as_view()),
    path('authors/<int:pk>/', AuthorDetailGeneric.as_view()),
    path('posts/', PostListGeneric.as_view()),
    path('posts/<int:pk>/', PostDetailGeneric.as_view()),
]
