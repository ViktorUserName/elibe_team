from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from bookmark.models import Bookmark
from bookmark.serializers import BookmarkReadSerializer, BookmarkWriteSerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return BookmarkReadSerializer
        return BookmarkWriteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)