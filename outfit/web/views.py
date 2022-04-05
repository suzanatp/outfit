from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from outfit.web.forms import CreateProfileForm, CreateOutfitForm, DeleteOutfitForm
from outfit.web.models import Profile, OutfitPhoto, Outfit


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


#
#
# def show_home(request):
#     # profile = get_profile()
#     # if not profile:
#     #     return redirect('create profile')
#     # context = {
#     #     'profile': profile,
#     #
#     # }
#     return render(request, 'base.html')


class HomeView(views.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('dashboard')
    #     return super().dispatch(request, *args, **kwargs)


class DashboardView(views.ListView):
    model = Outfit
    template_name = 'dashboard.html'
    context_object_name = 'outfit_photos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outfits'] = Outfit.objects.all()
        return context


class CreateOutfitView(views.CreateView):
    template_name = 'create_outfit.html'
    form_class = CreateOutfitForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditOutfitView(views.UpdateView):
    model = Outfit
    template_name = 'edit_outfit.html'
    success_url = reverse_lazy('dashboard')
    fields = '__all__'
    context_object_name = 'outfit'

    # form_class = EditOutfitForm

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['outfits'] = Outfit.objects.filter(pk=pk).get()
    #     return context


class DeleteOutfitView(views.DeleteView):
    template_name = 'delete_outfit.html'
    from_class = DeleteOutfitForm


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
