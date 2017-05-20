from django.core.management.base import BaseCommand
from nightreads.emails.models import Email
from nightreads.emails.email_service import send_email_obj
from nightreads.emails.views import get_subscriber_emails


class Command(BaseCommand):
    help = 'Send the email to susbcribers'

    def handle(self, *args, **options):
        email_obj = Email.objects.filter(is_sent=False).first()
        if not email_obj:
            return
        email_obj.recipients = get_subscriber_emails(email_obj=email_obj)
        send_email_obj(email_obj=email_obj)
        email_obj.is_sent = True
        email_obj.save()
        self.stdout.write(
            self.style.SUCCESS('Successfully sent email {}'.format(email_obj)))
