from django.contrib.auth.models import User

from nightreads.posts.models import Tag
from .models import (Subscription, EmailVerification)


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


def generate_email_verification_key(user):
    subscribe_key = User.objects.make_random_password(length=80)
    EmailVerification.objects.update_or_create(
        user=user, defaults={'subscribe_key': subscribe_key})
    return subscribe_key


def update_subscription(user, status):
    user.subscription.is_subscribed = status
    user.save()


def verify_subscription_code(user, code):
    if user.subscription.is_subscribed:
        return True


def verify_unsubscription_code(user, code):
    if not user.subscription.is_subscribed:
        return True
