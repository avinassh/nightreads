from django.contrib import admin
from django.conf.urls import url

from .models import Email
from .views import SendEmailAdminView
from .forms import EmailAdminForm


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

    def get_urls(self):
        urls = super(EmailAdmin, self).get_urls()
        my_urls = [
            url(r'^(?P<pk>\d+)/send_email/$',
                self.admin_site.admin_view(SendEmailAdminView.as_view()),
                name='send_email'),
        ]
        return my_urls + urls

admin.site.register(Email, EmailAdmin)
