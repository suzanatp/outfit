from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views import generic as views

from outfit.common.helpers import permissions_required
from outfit.web.forms import CreateOutfitPhotoForm
from outfit.web.models import OutfitPhoto, Outfit, Like, Dislike


class CreateOutfitPhotoView(LoginRequiredMixin, views.CreateView):
    template_name = 'web/photo/create_outfit_photo.html'
    form_class = CreateOutfitPhotoForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class EditOutfitPhotoView(LoginRequiredMixin, views.UpdateView):
    model = OutfitPhoto
    template_name = 'web/photo/edit_outfit_photo.html'
    success_url = reverse_lazy('dashboard')
    fields = '__all__'
    context_object_name = 'photo'


class DeleteOutfitPhotoView(LoginRequiredMixin, views.DeleteView):
    fields = '__all__'
    model = OutfitPhoto
    template_name = 'web/photo/delete_outfit_photo.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('dashboard')


def outfit_photos(request, pk):
    # likes = Like.objects.filter(user=request.user.id, photo=pk)
    outfit = Outfit.objects.get(pk=pk)
    photos = OutfitPhoto.objects.filter(outfit_id_id=pk)
    # comments = Comment.objects.all()
    user = request.user
    context = {
        'outfit': outfit,
        'photos': photos,
        'user_id': user,
        # 'likes': list(likes),
        # 'comments': comments,
        # 'comment_form': CommentForm()
    }
    return render(request, 'web/photo/outfit_photos.html', context)


class DetailsPhotoView(LoginRequiredMixin, views.DetailView):
    model = OutfitPhoto
    template_name = 'web/photo/details_outfit_photo.html'
    context_object_name = 'photo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'is_owner': self.object.user == self.request.user,
        })

        return context


@login_required(login_url=reverse_lazy('login user'))
@permissions_required(required_permissions=['web.add_like'])
def like_outfit_photo(request, pk):
    photo = OutfitPhoto.objects.get(pk=pk)
    dislike_object_by_user = photo.dislike_set.filter(user_id=request.user.id).first()
    like_object_by_user = photo.like_set.filter(user_id=request.user.id).first()
    if dislike_object_by_user:
        return redirect('details photo', photo.id)
    if like_object_by_user:
        like_object_by_user.delete()
    else:
        like = Like(
            photo=photo,
            user=request.user,
        )
        like.save()
    return redirect('details photo', photo.id)


@login_required(login_url=reverse_lazy('login user'))
@permissions_required(required_permissions=['web.add_dislike'])
def dislike_outfit_photo(request, pk):
    photo = OutfitPhoto.objects.get(pk=pk)
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
    return redirect('details photo', photo.id)
