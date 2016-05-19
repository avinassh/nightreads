from django import forms


class SubscribeForm(forms.Form):
    email = forms.EmailField()
    tags = forms.CharField()

    def clean_tags(self):
        tags = self.cleaned_data['tags'].split(',')
        return [t.strip().lower() for t in tags]


class UnsubscribeForm(forms.Form):
    email = forms.EmailField()
