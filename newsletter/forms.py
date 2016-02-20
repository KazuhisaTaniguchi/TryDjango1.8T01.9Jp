from django import forms
from .models import SingUp


class SingUpForm(forms.ModelForm):
    class Meta:
        model = SingUp
        fields = [
            'full_name',
            'email',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')

        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if not extension == 'edu':
            raise forms.ValidationError(
                'Please use a valid college email address')
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # Validation here
        return full_name
