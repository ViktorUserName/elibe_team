from rest_framework import viewsets, serializers
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
        if Bookmark.objects.filter(user=self.request.user, book=serializer.validated_data['book']).exists():
            raise serializers.ValidationError('This bookmark is already in this bookmark')
        serializer.save(user=self.request.user)