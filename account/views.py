from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from .serializers import (
    UserRegisterationSerializers,
    UserUpdateSerializer,
    UserDetailSerializer,
)
User = get_user_model()


@api_view(['GET'])
def accountOverview(request):
    account_urls = {
        'login': '/api/account/token/',
        'register': '/api/account/register/',
        'update profile': '/api/account/update/<int:pk>/'
    }
    return Response(account_urls)


@api_view(['POST'])
def accountRegister(request):
    serializer = UserRegisterationSerializers(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = 'Successfully register a new user'
    else:
        data = serializer.errors
    return Response(data)


@api_view(['PUT'])
def accountUpdate(request, pk):

    # try:
    #     user = get_object_or_404(User, id=pk)
    # except User.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    user = get_object_or_404(User, id=pk)
    serializer = UserUpdateSerializer(user, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.update(user, request.data)
        data['success'] = 'Your account update successfully'
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def accountUserDetail(request, pk):
    user = get_object_or_404(User, id=pk)
    data = {}
    serializer = UserDetailSerializer(user, many=False)
    data['userDetail'] = serializer.data
    return Response(data)


@api_view(['GET'])
def accountUsers(request):
    user = User.objects.all()
    serializer = UserDetailSerializer(user, many=True)
    data = {}
    data['users'] = serializer.data
    return Response(data)
