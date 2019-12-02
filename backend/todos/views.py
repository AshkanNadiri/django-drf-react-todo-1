from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Todo_Serializer
from .models import Todo

class Todo_Viewset(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = Todo_Serializer

# class User_Viewset( viewsets.ModelViewSet ):
    # queryset = User.objects.all().order_by('-date_joined')
    # serializer_class = User_Serializer

# Create your views here.
