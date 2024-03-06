from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from book.models import *
from book.serialazers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()
    data = []
    for book in books:
        data.append({
            'title': book.title,
            'author': book.author,
            'description': book.description
        })
    return Response(data=data, status=200)
@api_view(['POST'])
def book_create(request):
    data = request.data
    books = Book.objects.create(
        title=data['title'],
        description=data['description'],
        author=data['author']
    )
    return Response(data=books, status=201)
@api_view(['POST'])
def get_book(request, pk):
    id = request.POST.get('id')
    book = Book.objects.all()
    book_filter = Book.objects.filter(id=book.id)
    for book in book_filter:
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data, status=200)

@api_view(['POST'])
def get_book_order_genre(request):
    genre = request.POST.get('genre')
    books = Genre.objects.filter()
    serializer = BookSerializer(books, many=True)
    print(genre)
    return Response(serializer.data, status=200)


@api_view(['POST'])
def search_book(request):
    search = request.POST.get('search')
    book_filter = Book.objects.filter(title__icontains=search).order_by('title')
    serializer = BookSerializer(book_filter, many=True)
    return Response(serializer.data, status=200)




