from django.urls import path

from books_diary.book.views import BookByStatusListView

urlpatterns = (
    path('books/<str:status>/', BookByStatusListView.as_view(), name='book_by_status'),
)
