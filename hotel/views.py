from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .serializers import HotelSerializer
from .models import Hotel

# Create your views here.


@api_view(['GET'])
def hotels(request):
    hotels = Hotel.objects.all()
    serializer = HotelSerializer(hotels, many=True)
    data = {}
    data['hotels'] = serializer.data
    return Response(data, status=status.HTTP_200_OK)
