from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.contrib import auth
from django.views.generic import DeleteView

from outfit.accounts.forms import CreateProfileForm
from outfit.accounts.models import Profile
from outfit.common.view_mixins import RedirectToDashboard
from outfit.web.models import Outfit, OutfitPhoto

UserModel = get_user_model()


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
        user_photos = list(OutfitPhoto.objects.filter(user_id=self.object.user_id))

        outfit_photos = OutfitPhoto.objects \
            .filter(outfit_id_id__in=outfits) \
            .distinct()

        total_likes_count = sum(op.likes_count for op in outfit_photos)
        total_dislikes_count = sum(op.dislikes_count for op in outfit_photos) * (-1)
        total_comment_count = sum(o.comments_count for o in outfits)
        total_outfit_count = len(outfits)
        total_outfit_photos_count = len(outfit_photos)
        total_user_photos = len(user_photos)

        context.update({
            'total_likes_count': total_likes_count,
            'total_dislikes_count': total_dislikes_count,
            'total_outfit_count': total_outfit_count,
            'total_comment_count': total_comment_count,
            'total_outfit_photos_count': total_outfit_photos_count,
            'total_user_photos': total_user_photos,
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


class UserDeleteView(LoginRequiredMixin, DeleteView):
    """
    Simple confirmation view for user deletion.
    """
    model = UserModel
    template_name = 'accounts/delete_profile.html'

    def get_success_url(self):
        """
        Cleans the session on success
        :return: index url
        """
        logout(self.request)
        return reverse('index')

    def post(self, request, *args, **kwargs):
        """
        If 'cancel' in request redirects to update-profile view
        otherwise continues to success_url and user deletion
        :return:
        """
        if "cancel" in request.POST:
            return redirect('profile details', request.user.id)
        return super().post(request, *args, **kwargs)


class ChangeUserPasswordView(auth_views.PasswordChangeView):
    success_url = reverse_lazy('index')


def logout(request):
    auth.logout(request)
    return render(request, 'accounts/logout_page.html')
