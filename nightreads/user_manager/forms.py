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


class ConfirmEmailForm(forms.Form):
    email = forms.EmailField()
    subscribe = forms.IntegerField()
    code = forms.CharField(max_length=80)

    def clean_subscribe(self):
        value = bool(self.cleaned_data['subscribe'])
        self.cleaned_data['subscribe'] = value
        return value

    def clean(self):
        cleaned_data = super(ConfirmEmailForm, self).clean()
        if self.errors:
            return cleaned_data
        email = cleaned_data['email']
        code = cleaned_data['code']
        user = User.objects.filter(username=email).first()
        if not user:
            raise forms.ValidationError('Email not found')
        self.cleaned_data['user'] = user
        if user.emailverification.is_key_expired():
            raise forms.ValidationError('Link expired, please regenerate')
        if not user.emailverification.key == code:
            raise forms.ValidationError('Invalid Link')
        return cleaned_data
