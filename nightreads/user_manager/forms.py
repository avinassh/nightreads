from django.contrib.auth.models import User
from django import forms


class SubscribeForm(forms.Form):
    email = forms.EmailField()
    tags = forms.CharField()

    def clean_tags(self):
        tags = self.cleaned_data['tags'].split(',')
        return [t.strip().lower() for t in tags]


class UnsubscribeForm(forms.Form):
    email = forms.EmailField()


class ConfirmForm(forms.Form):
    email = forms.EmailField()
    code = forms.CharField(max_length=80)

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(username=email).first()
        if not user:
            raise forms.ValidationError('Email not found')
        self.cleaned_data['user'] = user
        return email
