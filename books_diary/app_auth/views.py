from django.contrib.auth import login, get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from django.views import generic as views

# app_auth models
UserModel = get_user_model()


class AnonymousUserMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_anonymous


class RegisterUserView(AnonymousUserMixin, views.View):
    pass


class LoginUserView(AnonymousUserMixin, auth_views.LoginView):
    template_name = 'app_auth/login.html'


class LogoutUserView(LoginRequiredMixin, auth_views.LogoutView):
    pass


class ChangePasswordView(LoginRequiredMixin, auth_views.PasswordChangeView):
    template_name = 'app_auth/change_password.html'
    success_url = reverse_lazy('logout_user')
