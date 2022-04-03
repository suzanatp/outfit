from django.shortcuts import render, redirect
from django.views import generic as views

from outfit.web.forms import CreateProfileForm
from outfit.web.models import Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


# def show_home(request):
#     profile = get_profile()
#     if not profile:
#         return redirect('create profile')
#     context = {
#         'profile': profile,
#
#     }
#     return render(request, 'base.html', context)


class HomeView(views.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = False
        return context


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(HomeView.as_view)
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
        'user': False,
    }
    return render(request, 'home-no-profile.html', context)
