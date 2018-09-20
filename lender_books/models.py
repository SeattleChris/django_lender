from django.db import models


class Book(models.Model):
    """ Each Book will have these properties.
    """
    STATES = [
        ('available', 'Available'),
        ('out', 'Checked out'),
    ]
    # cover_image = models.
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=48)
    year = models.IntegerField()
    status = models.CharField(choices=STATES, default='out', max_length=48)
    date_added = models.DateTimeField(auto_now_add=True)
    last_borrowed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Book: {self.title} | {self.author} | {self.year} | {self.status}'

    def __repr__(self):
        return f'Book: {self.title} | {self.author} | {self.year} | {self.status}'
