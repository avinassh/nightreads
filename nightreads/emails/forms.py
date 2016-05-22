from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Email


class EmailAdminForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Email
        widgets = {
            'message': SummernoteWidget()
        }
