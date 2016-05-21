from django.db import models

from nightreads.utils import TimeStampMixin
from nightreads.posts.models import Post


class Email(TimeStampMixin):
    subject = models.CharField(max_length=300)
    message = models.TextField()
    targetted_users = models.PositiveIntegerField(null=True)
    is_sent = models.BooleanField(default=False)

    post = models.ForeignKey(Post, null=True)
