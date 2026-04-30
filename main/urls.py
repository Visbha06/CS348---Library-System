from django.urls import path
from .views import book_list, add_book, edit_book, delete_book, add_genre, genre_list, edit_genre, delete_genre

urlpatterns = [
    path('', book_list),
    path('add/', add_book),
    path('edit/<int:book_id>/', edit_book),
    path('delete/<int:book_id>/', delete_book),
    path('add-genre/', add_genre),
    path('genres/', genre_list),
    path('edit-genre/<int:genre_id>/', edit_genre),
    path('delete-genre/<int:genre_id>/', delete_genre)
]