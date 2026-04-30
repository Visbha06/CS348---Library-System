from django import forms
from .models import Book, Genre

# Django handles input sanitisation as well
# Django forms validate integers, required fields, and max lengths
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'genre']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']