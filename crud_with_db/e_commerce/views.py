from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework import status

from .models import category as category_model


@api_view(['GET', 'POST'])
def get_categories_or_create_category(request: Request):
    data = []
    if request.method == 'GET':
        params = request.query_params
        
        category_objects = category_model.objects
        if params.get("name") is not None:
            category_objects = category_objects.filter(name=params.get("name"))

        if params.get("id") is not None:
            category_objects = category_objects.filter(id=params.get("id"))

        categories = category_objects.all()
        for category in categories:
            data.append({
                "id": category.id,
                "name": category.name,
                "created_at": category.created_at,
                "updated_at": category.updated_at
            })
    
    if request.method == 'POST':
        data = request.data

        category_model.objects.create(name=data.get("name"))

        data = "success"

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_category(request: Request, id):
    data = {}
    category = category_model.objects.get(pk=id)
    if request.method == 'GET':
        data = {
                "id": category.id,
                "name": category.name,
                "created_at": category.created_at,
                "updated_at": category.updated_at
            }
    
    if request.method == 'PUT':
        data = request.data
        name = data.get("name")
        category.name = name
        category.save()

        data = {
                "id": category.id,
                "name": category.name,
                "created_at": category.created_at,
                "updated_at": category.updated_at
            }


    if request.method == 'DELETE':
        category.delete()
        data = "deleted"
    return Response(data, status=status.HTTP_200_OK)