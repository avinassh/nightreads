from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Email
from .forms import EmailAdminForm
from nightreads.user_manager.models import Subscription


class SendEmailAdminView(View):

    template = 'admin/emails/email/send_email.html'
    form_class = EmailAdminForm

    def get(self, request, pk):
        email_obj = Email.objects.get(pk=pk)
        return render(request, self.template, {'email_obj': email_obj})

    def post(self, request, pk):
        email_type = request.POST.get('type', '').lower()
        email_obj = Email.objects.get(pk=pk)
        if email_type == 'preview':
            # send preview email
            m = 'Preview email has been sent!'
        else:
            # send email
            m = 'Email has been sent!'
            email_obj.is_sent = True
        messages.add_message(request, messages.INFO, m)
        return redirect(reverse(
            'admin:emails_email_change', args=(email_obj.id,)))


class UpdateTargetCountView(View):

    def get(self, request, pk):
        email_obj = Email.objects.get(pk=pk)
        email_obj.targetted_users = Subscription.objects.filter(
            Q(tags__in=email_obj.tags.all()) | Q(tags__name='all')).count()
        email_obj.save()
        return redirect(reverse(
            'admin:emails_email_change', args=(email_obj.id,)))


def _get_subscriber_emails(email_obj, count_only=False):
    queryset = Subscription.objects.filter(
        Q(tags__in=email_obj.tags.all()) | Q(tags__name='all'))
    if count_only:
        return queryset.count()
    return set(queryset.values_list('user__username', flat=True))
