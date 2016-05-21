from django.contrib import admin

from .models import Email


class EmailAdmin(admin.ModelAdmin):
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
