import json

from django.core.urlresolvers import reverse_lazy
from django.core import mail
from django.http import JsonResponse
from django.template.loader import render_to_string

from django.test import TestCase
from django.test.utils import override_settings

from . import user_service
from .forms import UnsubscribeForm


class UnsubscribePageBaseTest(TestCase):

    def setUp(self):
        self.page_url = reverse_lazy('users:unsubscribe')


class UnsubscribePageUnitTest(UnsubscribePageBaseTest):

    def test_unsubscribe_page_uses_correct_template(self):
        response = self.client.get(self.page_url)
        self.assertTemplateUsed(response, 'user_manager/unsubscribe.html')

    def test_unsubcribe_page_uses_unsubscribe_form(self):
        response = self.client.get(self.page_url)
        self.assertIsInstance(response.context['form'], UnsubscribeForm)

    def test_unsubscribe_form_submit_returns_json(self):
        response = self.client.post(self.page_url)
        self.assertIsInstance(response, JsonResponse)


class UnsubscribePageTest(UnsubscribePageBaseTest):

    def _get_response_json(self, response):
        return json.loads(response.content.decode('utf-8'))

    def test_validation_errors_on_empty_unsubscribe_form_submission(self):
        response_json = self._get_response_json(
            self.client.post(self.page_url)
        )
        self.assertIn('errors', response_json)

    def test_invalid_email_in_unsubscribe_form(self):
        response_json = self._get_response_json(
            self.client.post(self.page_url, data={'email': 'abcd'})
        )
        self.assertIn('errors', response_json)

    def test_unsubscribed_email_in_unsubscribe_form(self):
        response_json = self._get_response_json(
            self.client.post(self.page_url, data={'email': 'foo@example.com'})
        )
        self.assertIn('error', response_json)
        self.assertEqual(response_json['error'], 'User Not Found')

    @override_settings(
        EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
    )
    def test_successful_unsubscribe_form_submission(self):
        user_service.get_or_create_user(email='foo@example.com')

        response_json = self._get_response_json(
            self.client.post(self.page_url, data={'email': 'foo@example.com'})
        )
        self.assertIn('status', response_json)
        self.assertEqual(response_json['status'], 'Email sent')
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(
            mail.outbox[0].subject,
            render_to_string('user_manager/unsubscribe_subject.txt')
        )
