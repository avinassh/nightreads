from django.contrib.auth.models import User

from nightreads.posts.models import Tag
from .models import UserTags


def update_user_tags(user, tags):
    tags_objs = Tag.objects.filter(name__in=tags)
    user.usertags.tags.add(**tags_objs)
    user.save()


def get_user(email):
    user, created = User.objects.get_or_create(username=email)
    if created:
        UserTags.objects.create(user=user)
    return user
