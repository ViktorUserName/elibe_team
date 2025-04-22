from rest_framework import serializers

from book.models import Book
from book.serializers import BookSerializer
from bookmark.models import Bookmark

class BookShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']  # только id и имя

class BookmarkSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    book_detail = BookShortSerializer(source='book', read_only=True)

    class Meta:
        model = Bookmark
        fields = ['id', 'user', 'book', 'book_detail']
        read_only_fields = ['id', 'user']