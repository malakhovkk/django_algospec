from .models import Person
from rest_framework import serializers
from django import forms
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator

# class PersonSerializer(serializers.HyperlinkedModelSerializer):
#     password = serializers.CharField(
#         write_only=True,
#         required=True,
#     )
#     email = serializers.EmailField(
#             required=True,
#             validators=[UniqueValidator(queryset=Person.objects.all())]
#             )
#     username = serializers.CharField(
#             required=True,
#             validators=[UniqueValidator(queryset=Person.objects.all())]
#             )
#     password = serializers.CharField(min_length=8)
#     # def validate_unique(self, value):
#     #     if Person.filter
#     #     return value
#     class Meta:
#         model = Person
#         fields = ('username', 'email', 'password')
#     def create(self, validated_data):
#         validated_data['password'] = make_password(validated_data.get('password'))
#         return super(PersonSerializer, self).create(validated_data)