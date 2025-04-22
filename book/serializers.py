from rest_framework import serializers

from author.models import Author
from author.serializers import AuthorSerializer
from genres.models import Genre
from genres.serializers import GenresSerializer
from .models import Book

class BookReadSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    genres = GenresSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ('title', 'content', 'authors', 'genres')
        read_only_fields = ('id',)

class BookCreateSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, queryset=Author.objects.all())
    genres = serializers.PrimaryKeyRelatedField(many=True, queryset=Genre.objects.all())

    class Meta:
        model = Book
        fields = ('title', 'content', 'authors', 'genres')
