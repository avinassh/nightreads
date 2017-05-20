from django.contrib import admin

from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_subscribed']
    list_filter = ['is_subscribed']

admin.site.register(Subscription, SubscriptionAdmin)
