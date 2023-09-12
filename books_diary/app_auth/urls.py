from django.urls import path

from books_diary.app_auth.views import RegisterUserView, LoginUserView, LogoutUserView, ChangePasswordView

# app_auth urls
urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('logout/', LogoutUserView.as_view(), name='logout_user'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password')
)
