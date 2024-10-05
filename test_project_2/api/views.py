from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def product_deatils(request):
    person = [
        {
            "id": 1,
            "name": "Laptop",
            "category": "Electronics",
            "price": 999.99,
            "stock": 25,
            "rating": 4.7
        }]
    return Response(person)