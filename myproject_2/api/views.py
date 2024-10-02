from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request

@api_view(['GET'])
def getData(request : Request):
    person = [{"name": "danish", "email": "danish@gmail.com"}]
    return Response(person)