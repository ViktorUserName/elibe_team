from rest_framework import serializers

from book.serializers import BookSerializer
from bookmark.models import Bookmark


class BookmarkSerializer(serializers.ModelSerializer):
    # book = BookSerializer(read_only=True, many=True)
    class Meta:
        model = Bookmark
        fields = '__all__'
