from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateDestroyAPIView

from .models import Author, Post, Comment
from .serializers import AuthorSerializer, PostSerializer, CommentSerializer


class AuthorListGeneric(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PostListGeneric(ListCreateAPIView):
    template_name = "best_blog/posts_list.html"
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentListGeneric(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailGeneric(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


def home(request):
    return render(request, 'best_blog/posts_list.html')