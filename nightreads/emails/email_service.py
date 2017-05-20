from django.core.mail import send_mail
from django.conf import settings


def send_email(subject, message, recipient_list=(), preview=None):
    if preview:
        recipient_list = settings.PREVIEW_RECEPIENTS
    # TODO log this
    send_mail(
        subject=subject,
        message=message,
        html_message=message.replace('\n', '<br />'),
        from_email=settings.SENDER_EMAIL,
        recipient_list=recipient_list,
    )


def send_email_obj(email_obj, preview=None):
    if preview:
        email_obj.recipients = settings.PREVIEW_RECEPIENTS
    send_email(subject=email_obj.subject, message=email_obj.message,
               recipient_list=email_obj.recipients, preview=preview)