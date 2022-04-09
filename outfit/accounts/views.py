from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib import auth
from outfit.accounts.forms import CreateProfileForm
from outfit.accounts.models import Profile
from outfit.common.view_mixins import RedirectToDashboard
from outfit.web.models import Outfit, OutfitPhoto


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/registration_page.html'
    success_url = reverse_lazy('login user')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ProfileDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # self.object is a Profile instance
        outfits = list(Outfit.objects.filter(user_id=self.object.user_id))

        outfit_photos = OutfitPhoto.objects \
            .filter(outfit_id_id__in=outfits) \
            .distinct()

        total_likes_count = sum(op.likes_count for op in outfit_photos)
        total_dislikes_count = sum(op.dislikes_count for op in outfit_photos)*(-1)
        total_pet_photos_count = len(outfit_photos)

        context.update({
            'total_likes_count': total_likes_count,
            'total_dislikes_count': total_dislikes_count,
            'total_outfit_photos_count': total_pet_photos_count,
            'is_owner': self.object.user_id == self.request.user.id,
            'outfits': outfits,
        })

        return context


# def delete_profile(request):

class EditProfileView(views.UpdateView):
    model = Profile
    template_name = 'accounts/edit_profile_page.html'
    success_url = reverse_lazy('dashboard')
    fields = ('first_name', 'last_name', 'image', 'gender', 'email', 'age')
    context_object_name = 'outfit'


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    success_url = reverse_lazy('index')


def logout(request):
    auth.logout(request)
    return render(request, 'accounts/logout_page.html')
