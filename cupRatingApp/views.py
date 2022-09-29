from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cup
from .serializers import CupSerializer

@api_view(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def cups(request):
    print(request)
    if request.method == 'POST':
        serializer = CupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED, data=serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
    elif request.method == 'GET':
        all_cups = Cup.objects.all()
        serializer = CupSerializer(all_cups, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    elif request.method == 'DELETE':
        cup_to_delete = Cup.objects.get(uId=request.data['uId'])
        cup_to_delete.delete()
        return Response(status=status.HTTP_200_OK, data={'message': f'Cup with the uId ${request.data["uId"]} has '
                                                                    f'deleted'})
