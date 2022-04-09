from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from outfit.web.forms import CreateOutfitForm, CreateOutfitPhotoForm, CommentForm
from outfit.web.models import Outfit, OutfitPhoto, Like, Dislike, Comment


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
    context_object_name = 'outfit_photos'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['outfits'] = Outfit.objects.all()
    #
    #     return context


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


class DetailsOutfitView(LoginRequiredMixin, views.DetailView):
    model = Outfit
    template_name = 'web/outfit/details_outfit.html'
    context_object_name = 'outfit'

    # def dispatch(self, request, *args, **kwargs):
    #     response = super().dispatch(request, *args, **kwargs)
    #
    #     viewed_pet_photos = request.session.get('last_viewed_pet_photo_ids', [])
    #
    #     viewed_pet_photos.insert(0, self.kwargs['pk'])
    #     request.session['last_viewed_pet_photo_ids'] = viewed_pet_photos[:4]
    #
    #     return response
    #
    # def get_queryset(self):
    #     return super() \
    #         .get_queryset() \
    #         .prefetch_related('tagged_pets')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user == self.request.user

        return context


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
    # likes = Like.objects.filter(user=request.user.id, photo=pk)
    outfit = Outfit.objects.get(pk=pk)
    photos = OutfitPhoto.objects.all()
    # comments = Comment.objects.all()
    user = request.user
    context = {
        'outfit': outfit,
        'photos': list(photos),
        'user_id': user,
        # 'likes': list(likes),
        # 'comments': comments,
        # 'comment_form': CommentForm()
    }
    return render(request, 'web/outfit/outfit_photos.html', context)


@login_required(login_url=reverse_lazy('login user'))
def like_outfit_photo(request, pk):
    photo = OutfitPhoto.objects.get(pk=pk)
    outfit_id = photo.outfit_id_id
    dislike_object_by_user = photo.dislike_set.filter(user_id=request.user.id).first()
    like_object_by_user = photo.like_set.filter(user_id=request.user.id).first()
    if dislike_object_by_user:
        return redirect('outfit-photos', outfit_id)
    if like_object_by_user:
        like_object_by_user.delete()
    else:
        like = Like(
            photo=photo,
            user=request.user,
        )
        like.save()
    return redirect('outfit-photos', outfit_id)


@login_required(login_url=reverse_lazy('login user'))
def dislike_outfit_photo(request, pk):
    photo = OutfitPhoto.objects.get(pk=pk)
    outfit_id = photo.outfit_id_id
    dislike_object_by_user = photo.dislike_set.filter(user_id=request.user.id).first()
    like_object_by_user = photo.like_set.filter(user_id=request.user.id).first()
    if not like_object_by_user:
        if dislike_object_by_user:
            dislike_object_by_user.delete()
        else:
            dislike = Dislike(
                photo=photo,
                user=request.user,
            )
            dislike.save()
    return redirect('outfit-photos', outfit_id)


@login_required(login_url=reverse_lazy('login user'))
def comment_outfit_photo(request, pk):
    """
    This view does not render a template but saves the comment
    Relates the comment to the user and the recipe.
    If the form is invalid redirects to details view
    """
    outfit_photo = OutfitPhoto.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('outfit-photos', pk)
    else:
        form = CommentForm(request.POST)
    context = {
        'form': form,
        'outfit_photo': outfit_photo,

    }
    return render(request, 'web/outfit/comments_outfit_photo_add.html', context)
# class CreateCommentView(LoginRequiredMixin, views.CreateView):
#     template_name = 'web/outfit/comments_outfit_photo.html'
#     form_class = CommentForm
#     success_url = reverse_lazy('dashboard')
