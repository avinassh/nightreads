from django import forms


class SubscribeForm(forms.Form):
    email = forms.EmailField()
    tags = forms.CharField()

    def clean(self):
        tags = self.cleaned_data['tags'].split(',')
        self.cleaned_data['tags'] = [t.strip().lower() for t in tags]
        return self.cleaned_data
