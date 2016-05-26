from django.contrib import admin

from .models import Post, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_subscribers', 'get_posts')

    def get_subscribers(self, obj):
        return obj.subscription_set.count()
    get_subscribers.short_description = 'Subscribers'

    def get_posts(self, obj):
        return obj.post_set.count()
    get_posts.short_description = 'Posts'

admin.site.register(Post)
admin.site.register(Tag, TagAdmin)
