from django import forms

from outfit.common.helpers import BootstrapFormMixin
from outfit.web.models import Outfit, OutfitPhoto, Comment


class CreateOutfitForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        # commit false does not persist to database
        # just returns the object to be created
        outfit = super().save(commit=False)

        outfit.user = self.user
        if commit:
            outfit.save()

        return outfit

    class Meta:
        model = Outfit
        fields = ('name', 'category', 'season', 'weather')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter outfit name',
                }
            ),
        }


class CreateOutfitPhotoForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True, request=None):
        # commit false does not persist to database
        # just returns the object to be created
        outfit_photo = super().save(commit=False)

        outfit_photo.user = self.user
        if commit:
            outfit_photo.save()

        return outfit_photo

    class Meta:
        model = OutfitPhoto
        fields = ('photo', 'description', 'price', 'outfit_id')
        # fields = '__all__'
        widgets = {
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Enter description',
                }
            ),
        }


class CommentForm(BootstrapFormMixin, forms.ModelForm):
    """
    Form for creating a comment. Relates the comment to a recipe object
    """
    outfit_pk = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    class Meta:
        model = Comment
        fields = ('text', 'outfit_pk')

    def save(self, commit=True):
        """
        On save gets the recipe_pk from the view and
        assigns it to the comment
        """
        outfit_pk = self.cleaned_data['outfit_pk']
        outfit = Outfit.objects.get(pk=outfit_pk)
        comment = Comment(
            text=self.cleaned_data['text'],
            outfit=outfit,
        )

        if commit:
            comment.save()

        return comment

