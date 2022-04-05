from django import forms

from outfit.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from outfit.web.models import Profile, Outfit


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }

            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }

            ),
            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Email'
                }

            ),
            'age': forms.TextInput(
                attrs={
                    'placeholder': 'Age'
                }

            )
        }


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
        fields = ('name', 'category', 'season', 'user')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter outfit name',
                }
            ),
        }

#
# class EditOutfitForm(BootstrapFormMixin, forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self._init_bootstrap_form_controls()
#
#     class Meta:
#         model = Outfit
#         exclude = ('user_profile',)


class DeleteOutfitForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Outfit
        exclude = ('user_profile',)
