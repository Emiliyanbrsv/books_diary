from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('books_diary.book.urls')),
    path('', include('books_diary.app_auth.urls'))
]
