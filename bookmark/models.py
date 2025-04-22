from django.contrib.auth import get_user_model
from django.db import models

from author.models import Author
from book.models import Book

User = get_user_model()

class Bookmark(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='bookmarks')
    book = models.ForeignKey(Book,on_delete=models.CASCADE, related_name='bookmarks')


