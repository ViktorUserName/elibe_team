from rest_framework import serializers

from book.models import Book
from book.serializers import BookReadSerializer
from bookmark.models import Bookmark


class BookmarkReadSerializer(serializers.ModelSerializer):
    book_detail = BookReadSerializer(source='book', read_only=True)

    class Meta:
        model = Bookmark
        fields = '__all__'


class BookmarkWriteSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())

    class Meta:
        model = Bookmark
        fields = ['id', 'book']
        read_only_fields = ['id']