from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from book.models import Book
from book.serializers import BookReadSerializer, BookCreateSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return BookReadSerializer
        return BookCreateSerializer



