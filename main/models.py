from django.db import models

# Create your models here.

# Django automatically creates primary keys (ids) for each class

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE) # Foreign Key

    class Meta:
        indexes = [
            models.Index(fields=['genre']),
            models.Index(fields=['publication_year']),
            models.Index(fields=['genre', 'publication_year']),
        ]

    def __str__(self):
        return self.title