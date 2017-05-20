from django.db import models

from nightreads.utils import TimeStampMixin


class Tag(TimeStampMixin):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Email(TimeStampMixin):
    subject = models.CharField(max_length=300)
    message = models.TextField()
    targetted_users = models.PositiveIntegerField(null=True)
    is_sent = models.BooleanField(default=False)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "{} - {}".format(self.id, self.subject)
