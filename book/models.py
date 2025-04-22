from django.db import models
from author.models import Author
from genres.models import Genre


class Book(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    author = models.ManyToManyField(Author, related_name='books')
    genres = models.ManyToManyField(Genre, related_name='books')

    def __str__(self):
        return self.title