from rest_framework import viewsets

from elibe.permissions import IsAdminOrReadOnly
from genres.models import Genre
from genres.serializers import GenresSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer
    permission_classes = [IsAdminOrReadOnly]

