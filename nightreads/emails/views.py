from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Email
from .forms import EmailAdminForm


class SendEmailAdminView(View):

    template = 'admin/emails/email/send_email.html'
    form_class = EmailAdminForm

    def get(self, request, pk):
        email_obj = Email.objects.get(pk=pk)
        return render(request, self.template, {'email_obj': email_obj})

    def post(self, request, pk):
        email_obj = Email.objects.get(pk=pk)
        email_obj.is_sent = True
        # send email
        messages.add_message(request, messages.INFO, 'Email has been sent!')
        return redirect(reverse(
            'admin:emails_email_change', args=(email_obj.id,)))
