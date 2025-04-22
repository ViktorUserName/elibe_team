from django.contrib.auth import get_user_model
from django.db import models

from author.models import Author
from book.models import Book

User = get_user_model()

class Bookmark(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='bookmarks')
    books = models.ForeignKey(Book,on_delete=models.CASCADE, related_name='bookmarks')

    class Meta:
        unique_together = ('user', 'books')

    def __str__(self):
        return f'{self.user.username} - {self.books.title}'

