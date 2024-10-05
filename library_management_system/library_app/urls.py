from django.urls import path
from . import views

urlpatterns = [
    path("authors/", views.get_all_authors_or_create_author),
    path("authors/<int:id>/", views.get_or_update_or_delete_author),
    path("genres/", views.get_all_genres_or_create_genre),
    path("genres/<int:id>/", views.get_or_update_or_delete_genre),
    path("books/", views.get_all_books_or_create_book),
    path("books/<int:id>/", views.get_or_update_or_delete_book)
]