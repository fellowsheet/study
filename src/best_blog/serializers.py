from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'first_name', 'last_name', 'middle_name', 'avatar', 'birth_date',
            'user', 'slug')
