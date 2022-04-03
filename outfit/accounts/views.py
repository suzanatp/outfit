from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from outfit.web.views import HomeView


class UserRegisterView:
    pass


class UserLoginView(auth_views.LoginView):
    template_name = 'login_page.html'
    success_url = reverse_lazy(HomeView.as_view)

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserProfileView:
    pass


class EditProfileView:
    pass


class ChangeUserPasswordView:
    pass
