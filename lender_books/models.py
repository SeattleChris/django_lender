from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver  # decorator
from django.utils import timezone

class Book(models.Model):
    """ Each Book will have these properties.
        STATES will be a drop-down list for where it is placed
    """
    STATES = [
        ('available', 'Available'),
        ('out', 'Checked out'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0, related_name='books')
    title = models.CharField(max_length=48)
    # cover_image = models. ...
    author = models.CharField(max_length=48)
    year = models.IntegerField()
    status = models.CharField(choices=STATES, default='out', max_length=48)
    date_added = models.DateTimeField(auto_now_add=True)
    last_borrowed = models.DateTimeField(blank=True, null=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Book: {self.title} | {self.author} | {self.year} | {self.status}'

    def __repr__(self):
        return f'Book: {self.title} | {self.author} | {self.year} | {self.status}'


@receiver(models.signals.post_save, sender=Book)
def set_book_checked_out_date(sender, instance, **kwargs):
    if instance.status == 'out'and not instance.last_borrowed:
        instance.last_borrowed = timezone.now
        instance.save()
