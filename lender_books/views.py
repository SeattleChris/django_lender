from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.exceptions import PermissionDenied
from .models import Book


def book_list_view(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    # books = Book.objects.all()
    books = Book.objects.filter(user_username=request.user.username)
    context = {
        'books': books
    }
    return render(request, 'book_list.html', context=context)


def book_detail_view(request, pk=None):
    if not request.user.is_authenticated:
        return redirect(reverse('login'))
    # book = get_object_or_404(Book, id=pk)
    book = get_object_or_404(Book, id=pk, user_ud=request.user.id)
    context = {
        'book': book,
    }
    return render(request, 'book_detail.html', context=context)
