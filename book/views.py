from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from book.models import Book
from book.serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



