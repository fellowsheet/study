from rest_framework import serializers
from .models import Author, Post


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'first_name', 'last_name', 'middle_name', 'avatar', 'birth_date',
            'user', 'slug')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
