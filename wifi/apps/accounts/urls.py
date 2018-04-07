from django.conf.urls import url
from django.contrib.auth.views import logout

from wifi.apps.accounts.views import LoginPage

app_name = 'accounts'

urlpatterns = [
    url(r'^login/$', LoginPage.as_view(), name='login'),
    url(r'^logout/$', logout, {'next_page': '/login'}, name='logout')
]
