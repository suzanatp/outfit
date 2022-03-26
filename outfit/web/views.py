from django.shortcuts import render, redirect

from outfit.web.forms import CreateProfileForm
from outfit.web.models import Profile


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    context = {
        'profile': profile,

    }
    return render(request, 'base.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = CreateProfileForm()
    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html',context)