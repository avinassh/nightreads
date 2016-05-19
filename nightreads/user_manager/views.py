from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .forms import SubscribeForm, UnsubscribeForm, ConfirmEmailForm
from . import user_service


class SubscribeView(View):
    form_class = SubscribeForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SubscribeView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            tags = form.cleaned_data['tags']
            user = user_service.get_or_create_user(email=email)
            is_updated = user_service.update_user_tags(user=user, tags=tags)
            if is_updated:
                key = user_service.generate_key(user=user)
                return JsonResponse({'success': key})
            return JsonResponse({'success': False})


class UnsubscribeView(View):

    form_class = UnsubscribeForm

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(UnsubscribeView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = user_service.get_user(email=email)
            if not user:
                return JsonResponse({'success': False})
            return JsonResponse({'success': True})


class ConfirmEmailView(View):

    form_class = ConfirmEmailForm

    def get(self, request):
        form = self.form_class(request.GET)
        if form.is_valid():
            if form.cleaned_data['subscribe']:
                return JsonResponse({'status': 'Subscribed'})
            else:
                return JsonResponse({'status': 'Unsubscribed'})
        return JsonResponse({'success': form.errors})
