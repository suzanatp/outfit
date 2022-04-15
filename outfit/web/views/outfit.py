from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from outfit.common.helpers import permissions_required
from outfit.web.forms import CreateOutfitForm, CommentForm
from outfit.web.models import Outfit, Comment


class CreateOutfitView(LoginRequiredMixin, views.CreateView):
    template_name = 'web/outfit/create_outfit.html'
    form_class = CreateOutfitForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class DetailsOutfitView(LoginRequiredMixin, views.DetailView):
    model = Outfit
    template_name = 'web/outfit/details_outfit.html'
    context_object_name = 'outfit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'comments': self.object.comment_set.all(),
            'comment_form': CommentForm(
                initial={'outfit_pk': self.object.pk}
            ),
            'is_owner': self.object.user == self.request.user,
        })

        return context


class EditOutfitView(LoginRequiredMixin, views.UpdateView):
    model = Outfit
    template_name = 'web/outfit/edit_outfit.html'
    success_url = reverse_lazy('dashboard')
    fields = '__all__'
    context_object_name = 'outfit'


class DeleteOutfitView(LoginRequiredMixin, views.DeleteView):
    fields = '__all__'
    model = Outfit
    template_name = 'web/outfit/delete_outfit.html'
    success_url = reverse_lazy('dashboard')


@login_required(login_url=reverse_lazy('login user'))
@permissions_required(required_permissions=['web.add_comment'])
def comment_outfit(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()
    return redirect('details outfit', pk)


@login_required(login_url=reverse_lazy('login user'))
@permissions_required('web.delete_comment')
def delete_comment(request, outfit_pk, comment_pk):
    """
    On success deletes the comment with the given pk.
    Ensures that user is able to delete only their own comments.
    """
    comment = Comment.objects.get(pk=comment_pk)
    if request.user.id == comment.user.id:
        comment.delete()
    return redirect('details outfit', outfit_pk)
