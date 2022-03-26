from django import forms

from outfit.web.models import Profile


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

