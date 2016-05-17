from django.db import models
from django.contrib.auth.models import User

from nightreads.utils import TimeStampMixin
from nightreads.posts.models import Tag


class UserTags(TimeStampMixin):
    user = models.OneToOneField(User)
    tags = models.ManyToManyField(Tag)
