from django.test import TestCase, RequestFactory
from .models import Book

# title = models.CharField(max_length=48)
# author = models.CharField(max_length=48)
# year = models.IntegerField(max_length=4)


class TestBookModel(TestCase):
    """ Currently Book model has: title, author, year, status (default='out')
        plus 2 more auto-populated: date_added and last_borrowed
    """
    def setUp(self):
        """ We can use these temporary books for testing
        """
        self.book = Book.objects.create(title='Book Test', author='Ms Author', year='2018')
        Book.objects.create(title='Another Book', author='Another Author', year='2016')
        Book.objects.create(title='Old Test Book', description='Ms Author', year='2014')

    def test_book_titles(self):
        """ Do we accuratly see the title
        """
        self.assertEqual(self.note.title, 'Book Test')

#     def test_book_author(self):
#         """ For an existing book of a certain title, do we accuratly see the author
#         """
#         book = Book.objects.get(title='Another Book')
#         self.assertEqual(book.author, 'Another Author')


# class TestBookViews(TestCase):
#     """ Testong the views. Currently we have 2:
#         book_detail_view, book_list_view
#     """
#     def setUp(self):
#         """ We can use these temporary books for testing
#         """
#         self.request = RequestFactory()
#         self.book_one = Book.objects.create(title='Green Eggs and Ham', author='Dr Suess', year='1960')
#         self.book_two = Book.objects.create(title='I, Robot', author='Isaac Asimov', year='1950')

#     def test_book_detail_view(self):
#         """ Get the first book and verify the title has a certain word in it
#         """
#         from .views import book_detail_view
#         request = self.request.get('')
#         response = book_detail_view(request, f'{self.book_one.id}')
#         self.assertIn(b'Eggs', response.content)

#     def test_note_detail_status(self):
#         """ Do we get a status 200 response
#         """
#         from .views import notes_detail_view
#         request = self.request.get('')
#         response = notes_detail_view(request, f'{self.book_one.id}')
#         self.assertEqual(200, response.status_code)

#     def test_book_list_view(self):
#         """ From the full book list, does one of the books have the known title
#         """
#         from .views import book_list_view
#         request = self.request.get('')
#         response = book_list_view(request)
#         self.assertIn(b'Robot', response.content)

#     def test_book_list_status(self):
#         """ Do we get a status 200 response on list
#         """
#         from .views import book_list_view
#         request = self.request.get('')
#         response = book_list_view(request)
#         self.assertEqual(200, response.status_code)
