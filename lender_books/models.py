from django.db import models


class Book(models.Model):
    """
    """
    STATES = [
        ('incomplete', 'Incomplete'),
        ('complete', 'Complete'),
    ]

    title = models.CharField(max_length=48)
    description = models.CharField(max_length=4096)
    status = models.CharField(choices=STATES, default='incomplete', max_length=48)

    def __str__(self):
        pass

    def __repr__(self):
        pass
