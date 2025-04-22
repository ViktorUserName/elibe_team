from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.name = self.name.strip().capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
