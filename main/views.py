from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .models import Book, Genre
from .forms import BookForm, GenreForm

# This database uses the isolation level READ COMMITTED (Django default).
# Designed for multiple users accessing the same database concurrently.
# READ COMMITTED isolation prevents dirty reads, allows repeatable reads while 
# maintaining good performance.

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    genres = Genre.objects.all()

    min_year = request.GET.get('min_year')
    max_year = request.GET.get('max_year')
    genre_id = request.GET.get('genre')

    # Django ORM uses prepared statements automatically. It never concatenates raw SQL strings

    # Never concatenate raw SQL strings. Example:
    # f"SELECT * FROM book WHERE title = '{user_input}'"
    # This is vulnerable to SQL injection attacks
    if min_year:
        books = books.filter(publication_year__gte=min_year)
    if max_year:
        books = books.filter(publication_year__lte=max_year)
    if genre_id:
        books = books.filter(genre_id=genre_id)

    context = {
        'books': books,
        'genres': genres,
        'min_year': min_year,
        'max_year': max_year,
        'selected_genre': genre_id
    }

    return render(request, 'main/book_list.html', context)

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()

    return render(request, 'main/add_book.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm(instance=book)

    return render(request, 'main/edit_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('/')
    
    return render(request, 'main/delete_book.html', {'book': book})

def genre_list(request):
    genres = Genre.objects.all()
    return render(request, 'main/genre_list.html', {'genres': genres})

def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = GenreForm()

    return render(request, 'main/add_genre.html', {'form': form})

def edit_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)

    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('/genres/')
    else:
        form = GenreForm(instance=genre)

    return render(request, 'main/edit_genre.html', {'form': form, 'genre': genre})

def delete_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)

    # Only use atomic transactions when multiple related database operations must succeed
    # or fail together, such as cascading deletes
    if request.method == 'POST':
        with transaction.atomic():
            genre.delete()
        return redirect('/genres/')
    
    return render(request, 'main/delete_genre.html', {'genre': genre})