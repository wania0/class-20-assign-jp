from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Authors as authors_model
from .models import Genres as genres_model
from .models import Books as books_model

# authors
@api_view(['GET', 'POST'])
def get_all_authors_or_create_author(request: Request):
    data = []
    
    if request.method == 'GET':
        author_object = authors_model.objects
        authors = author_object.all()
        for author in authors:
            data.append({
                "id": author.id,
                "name": author.name,
                "bio" : author.bio
            })
    
    if request.method == 'POST':
        data = request.data

        authors_model.objects.create(name=data.get("name"))
        data = "author created succesfully"

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_author(request: Request, id):
    data = {}
    
    author = authors_model.objects.get(pk=id)
    if request.method == 'GET':
        data = {
                "id": author.id,
                "name": author.name,
                "bio" : author.bio
            }
    
    if request.method == 'PUT':
        data = request.data
        name = data.get("name")
        author.name = name
        author.save()
        
        data = {
                "id": author.id,
                "name": author.name,
                "bio" : author.bio
            }


    if request.method == 'DELETE':
        author.delete()
        data = "deleted"
    return Response(data, status=status.HTTP_200_OK)




# genres
@api_view(['GET', 'POST'])
def get_all_genres_or_create_genre(request: Request):
    data = []
    
    if request.method == 'GET':
        genre_object = genres_model.objects
        genres = genre_object.all()
        for genre in genres:
            data.append({
                "id": genre.id,
                "name": genre.name
            })
    
    if request.method == 'POST':
        data = request.data

        genres_model.objects.create(name=data.get("name"))
        data = "genre created succesfully"

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_genre(request: Request, id):
    data = {}
    
    genre = genres_model.objects.get(pk=id)
    if request.method == 'GET':
        data = {
                "id": genre.id,
                "name": genre.name
                }
    
    if request.method == 'PUT':
        data = request.data
        name = data.get("name")
        genre.name = name
        genre.save()
        
        data = {
                "id": genre.id,
                "name": genre.name
            }


    if request.method == 'DELETE':
        genre.delete()
        data = "deleted"
    return Response(data, status=status.HTTP_200_OK)




# books
@api_view(['GET', 'POST'])
def get_all_books_or_create_book(request: Request):
    data = []
    if request.method == 'GET':
        params = request.query_params
        
        book_objects = books_model.objects
        if params.get("title") is not None:
            book_objects = book_objects.filter(title=params.get("title"))

        if params.get("author_id") is not None:
           book_objects = book_objects.filter(author_id=params.get("author_id"))
           
        if params.get("genre_id") is not None:
            book_objects = book_objects.filter(genre_id=params.get("genre_id"))
            
        if params.get("published_date") is not None:
            book_objects = book_objects.filter(published_date=params.get("published_date"))

        books = book_objects.all()
        for book in books:
            data.append(
                {
                "id": book.id,
                "title": book.title,
                "author_id" : book.author_id,
                "genre_id" : book.genre_id,
                "published_date" : book.published_date
            }
            )
    
    
    if request.method == 'POST':
        data = request.data

        books_model.objects.create(title=data.get("title"))
        books_model.objects.create(author_id=data.get("author_id"))
        books_model.objects.create(genre_id=data.get("genre_id"))
        data = "book created succesfully"

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_book(request: Request, id):
    data = {}
    
    book = books_model.objects.get(pk=id)
    if request.method == 'GET':
        data = {
                "id": book.id,
                "title": book.title,
                "author_id" : book.author_id,
                "genre_id" : book.genre_id,
                "published_date" : book.published_date
            }
    
    if request.method == 'PUT':
        data = request.data
        title = data.get("title")
        author_id = data.get("author_id")
        genre_id = data.get("genre_id")
        book.title = title
        book.author_id = author_id
        book.genre_id = genre_id
        book.save()
        
        data = {
                "id": book.id,
                "title": book.title,
                "author_id" : book.author_id,
                "genre_id" : book.genre_id,
                "published_date" : book.published_date
            }


    if request.method == 'DELETE':
        book.delete()
        data = "deleted"
    return Response(data, status=status.HTTP_200_OK)