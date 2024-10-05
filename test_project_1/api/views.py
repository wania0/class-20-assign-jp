from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def my_info(request):
    person = [{"Name": "Wania Sarfaraz", "Email": "wania@gmail.com"}]
    return Response(person)