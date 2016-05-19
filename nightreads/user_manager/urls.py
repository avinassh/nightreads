from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'unsubscribe/', views.UnsubscribeView.as_view(), name='unsubscribe'),
    url(r'subscribe/', views.SubscribeView.as_view(), name='subscribe'),
]
