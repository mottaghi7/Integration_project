from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from UserManager import models as user_manager_model
import api.serializers as serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = user_manager_model.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserLoginViewSet(viewsets.ViewSet):
    serializer_class = serializers.LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({
                'user': str(user.id)
            })

        return Response({
            'response': 'user not found'
        })


class UserLogoutViewSet(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        if request.user is not None:
            user = request.user
            logout(request)
            return Response({
                'user': str(user.id)
            })

        return Response({
            'response': 'user not login'
        })
