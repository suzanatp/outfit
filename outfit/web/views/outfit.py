from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from outfit.web.forms import  CreateOutfitForm, CreateOutfitPhotoForm
from outfit.web.models import Outfit, OutfitPhoto


class HomeView(views.TemplateView):
    template_name = 'web/home.html'

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
    template_name = 'web/dashboard.html'

    # context_object_name = 'outfit_photos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outfits'] = Outfit.objects.all()
        return context


class CreateOutfitView(LoginRequiredMixin, views.CreateView):
    template_name = 'web/outfit/create_outfit.html'
    form_class = CreateOutfitForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['is_owner'] = self.object.user == self.request.user
    #
    #     return context


class EditOutfitView(views.UpdateView):
    model = Outfit
    template_name = 'web/outfit/edit_outfit.html'
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
    fields = '__all__'
    model = Outfit
    template_name = 'web/outfit/delete_outfit.html'
    success_url = reverse_lazy('dashboard')


class DeleteOutfitPhotoView(views.DeleteView):
    fields = '__all__'
    model = OutfitPhoto
    template_name = 'web/outfit/delete_outfit_photo.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('dashboard')


class CreateOutfitPhotoView(LoginRequiredMixin, views.CreateView):
    template_name = 'web/outfit/create_outfit_photo.html'
    form_class = CreateOutfitPhotoForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditOutfitPhotoView(LoginRequiredMixin, views.UpdateView):
    model = OutfitPhoto
    template_name = 'web/outfit/edit_outfit_photo.html'
    success_url = reverse_lazy('dashboard')
    fields = '__all__'
    context_object_name = 'photo'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['is_owner'] = self.object.user == self.request.user
    #
    #     return context


def outfit_photos(request, pk):
    outfit = Outfit.objects.get(pk=pk)
    photos = OutfitPhoto.objects.all()
    context = {
        'outfit': outfit,
        'photos': list(photos),
    }
    return render(request, 'web/outfit/outfit_photos.html', context)

#
# def create_profile(request):
#     if request.method == 'POST':
#         form = CreateProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(HomeView.as_view)
#     else:
#         form = CreateProfileForm()
#     context = {
#         'form': form,
#         'user': False,
#     }
#     return render(request, 'web/home-no-profile.html', context)
