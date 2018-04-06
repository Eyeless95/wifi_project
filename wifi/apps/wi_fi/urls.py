from django.conf.urls import url

from wifi.apps.wi_fi.views import Advertisement, ThankYouPage, callback_and_redirect

app_name = 'wi_fi'

urlpatterns = [
    url(r'^connect_to_wifi/$', Advertisement.as_view(), name='landing'),
    url(r'^callback_and_redirect/$', callback_and_redirect, name='callback'),
    url(r'^success_page/$', ThankYouPage.as_view(), name='success_page')
]
