from rest_framework import serializers, fields
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from UserManager import models as user_manager_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_manager_model.User
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=1000)
    password = serializers.CharField(max_length=1000)

# class UserManageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ('email', 'password', 'saved_cooking_instruction', 'exist_raw_material')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = get_user_model().objects.create_user(validated_data['email'], validated_data['password'])
#         return user
#
#     def update(self, instance, validated_data):
#         instance.email = validated_data['email']
#         for attr, value in validated_data.items():
#             if attr == 'password':
#                 instance.set_password(value)
#         instance.save()
#         instance.saved_cooking_instruction.set(validated_data['saved_cooking_instruction'])
#         instance.exist_raw_material.set(validated_data['exist_raw_material'])
#
#         return instance
