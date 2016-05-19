from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

from nightreads.utils import TimeStampMixin
from nightreads.posts.models import Tag


class Subscription(TimeStampMixin):
    is_subscribed = models.BooleanField(default=False)
    user = models.OneToOneField(User)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.user.username


class EmailVerificationMixin(models.Model):
    generated_on = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User)

    def is_key_expired(self):
        current_time = timezone.now()
        delta = current_time - self.generated_on
        if delta.days > settings.EMAIL_LINK_EXPIRY_DAYS:
            return True
        return False

    class Meta:
        abstract = True


class SubscriptionActivation(EmailVerificationMixin):
    subscribe_key = models.CharField(max_length=80)


class UnsubscriptionActivation(EmailVerificationMixin):
    unsubscribe_key = models.CharField(max_length=80)
