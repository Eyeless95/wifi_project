from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from wifi.apps.dashboard.views import Dashboard, ajax_dashboard_datatable

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', login_required(Dashboard.as_view()), name='dashboard'),
    url(r'^ajax_dashboard_datatable/$', login_required(ajax_dashboard_datatable), name='ajax_dashboard_datatable')
]
