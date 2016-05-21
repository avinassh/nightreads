from django.contrib import admin
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from .models import Email


class EmailAdminForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Email
        widgets = {
            'message': SummernoteWidget()
        }


class EmailAdmin(admin.ModelAdmin):
    form = EmailAdminForm
    readonly_fields = ('targetted_users', 'is_sent',)
    add_fieldsets = (
        (None, {
            'fields': ('subject', 'message', 'post'),
        }),
    )

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super(EmailAdmin, self).get_fieldsets(request, obj)


admin.site.register(Email, EmailAdmin)
