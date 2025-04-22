from rest_framework import viewsets

from author.models import Author
from author.serializers import AuthorSerializer
from elibe.permissions import IsAdminOrReadOnly


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]

