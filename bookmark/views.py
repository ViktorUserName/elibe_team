from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from book.models import Book
from book.serializers import BookSerializer
from bookmark.models import Bookmark
from bookmark.serializers import BookmarkSerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)