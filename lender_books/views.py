from django.shortcuts import render
from .models import Book


def book_list_view(request):
    books = Book.objects.all()
    context = {
        'books': books
    }

    return render(request, 'books/books_list.html', context=context)


def book_detail_view(request, pk=None):
    pass





