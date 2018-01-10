# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer


class BooksView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
