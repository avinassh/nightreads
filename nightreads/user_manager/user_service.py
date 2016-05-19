from django.contrib.auth.models import User
from django.conf import settings
from django.core.signing import TimestampSigner

from nightreads.posts.models import Tag
from .models import Subscription


def update_user_tags(user, tags):
    tags_objs = Tag.objects.filter(name__in=tags)
    if tags_objs:
        user.subscription.tags.clear()
        user.subscription.tags.add(*tags_objs)
        user.save()
        return True
    return False


def get_or_create_user(email):
    user, created = User.objects.get_or_create(username=email)
    if created:
        Subscription.objects.create(user=user)
    return user


def get_user(email):
    return User.objects.filter(username=email).first()


def generate_key(user, for_subscription=True):
    salt = 'subscription' if for_subscription else 'unsubscription'
    signer = TimestampSigner(settings.SECRET_KEY, salt=salt)
    return signer.sign(str(user.id))


def validate_key(key, user, for_subscription=True):
    salt = 'subscription' if for_subscription else 'unsubscription'
    signer = TimestampSigner(settings.SECRET_KEY, salt=salt)
    value = signer.unsign(key, max_age=settings.EMAIL_LINK_EXPIRY_DAYS)
    return str(user.id) == value


def update_subscription(user, status):
    user.subscription.is_subscribed = status
    user.save()


def verify_subscription_code(user, code):
    if user.subscription.is_subscribed:
        return True


def verify_unsubscription_code(user, code):
    if not user.subscription.is_subscribed:
        return True
