from django.contrib.auth.models import User

from nightreads.posts.models import Tag
from .models import UserTag


def update_user_tags(user, tags):
    tags_objs = Tag.objects.filter(name__in=tags)
    user.usertag.tags.add(*tags_objs)
    user.save()


def get_user(email):
    user, created = User.objects.get_or_create(username=email)
    if created:
        UserTag.objects.create(user=user)
    return user
