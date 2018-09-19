from .views import book_list_view, book_detail_view
from django.urls import path

urlpatterns = [
    path('', book_list_view, name='books_list')
    path('<int:pk>', books_detail_view, name='books_detail'),
]