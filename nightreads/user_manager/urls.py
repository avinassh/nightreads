from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'$', views.SubscribeView.as_view(), name='subscribe'),
]
