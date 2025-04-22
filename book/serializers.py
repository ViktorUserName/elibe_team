from rest_framework import serializers

from author.models import Author
from author.serializers import AuthorSerializer
from genres.serializers import GenresSerializer
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True, many=True)
    genres = GenresSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = ('title', 'content', 'author', 'genres')
        read_only_fields = ('id',)

    def perform_delete(self):
        pass