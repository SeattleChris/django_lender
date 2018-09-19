from django.shortcuts import render, get_object_or_404
from .models import Book


def book_list_view(request):
    books = Book.objects.all()
    context = {
        'books': books
    }

    return render(request, 'books/books_list.html', context=context)


def book_detail_view(request, pk=None):
    book = get_object_or_404(Books, id=pk)
    context = {
        'book': book
    }

    return render(request, 'books/books_detail.html', context=context)




