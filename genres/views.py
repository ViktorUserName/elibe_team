from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from genres.models import Genre


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
