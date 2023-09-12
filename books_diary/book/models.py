from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=100
    )

    author = models.CharField(
        max_length=50
    )

    publication_date = models.DateField()

    genre = models.CharField(
        max_length=50
    )

    pages = models.PositiveIntegerField()

    READ_STATUS_CHOICES = [
        ('Reading', 'Reading'),
        ('Read', 'Read'),
        ('To Read', 'To Read'),
    ]

    status = models.CharField(
        max_length=30,
        choices=READ_STATUS_CHOICES,
        default='To Read'
    )

    def __str__(self):
        return f"{self.pk}. {self.title}"

    class Meta:
        ordering = ['pk']
