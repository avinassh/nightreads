from django.contrib.auth.models import User
from django.core.signing import BadSignature, SignatureExpired
from django import forms

from nightreads.posts.models import Tag
from . import user_service


class SubscribeForm(forms.Form):
    email = forms.EmailField()

    def clean(self):
        cleaned_data = super(SubscribeForm, self).clean()
        all_tag, _ = Tag.objects.get_or_create(name='all')
        cleaned_data['tags'] = [all_tag, ]
        return cleaned_data


class UnsubscribeForm(forms.Form):
    email = forms.EmailField()


class ConfirmEmailForm(forms.Form):
    user = forms.IntegerField()
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
        user_id = cleaned_data['user']
        code = cleaned_data['code']
        for_subscription = cleaned_data['subscribe']
        user = User.objects.filter(id=user_id).first()
        if not user:
            raise forms.ValidationError('Invalid Link')
        self.cleaned_data['user'] = user
        try:
            user_service.validate_key(key=code, user=user,
                                      for_subscription=for_subscription)
        except BadSignature:
            raise forms.ValidationError('Invalid Link')
        except SignatureExpired:
            raise forms.ValidationError('Link expired, please regenerate')
        return cleaned_data
