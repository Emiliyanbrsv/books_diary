from django.shortcuts import render
from django.views import generic as views

from books_diary.book.models import Book


class BookByStatusListView(views.ListView):
    model = Book
    template_name = 'book/book_by_status_list.html'

    def get_queryset(self):
        book_status = self.kwargs['status']  # Get the status from the URL parameter
        return Book.objects.filter(status=book_status)
