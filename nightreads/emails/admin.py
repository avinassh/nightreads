from django.contrib import admin

from .models import Email


class EmailAdmin(admin.ModelAdmin):
    exclude = ('targetted_users', 'is_sent')

admin.site.register(Email, EmailAdmin)
