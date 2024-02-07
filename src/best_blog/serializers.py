from rest_framework import serializers
from .models import Author, Post, Comment


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'first_name', 'last_name', 'middle_name', 'avatar', 'birth_date',
            'user', 'slug')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.first_name', read_only=True)
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

