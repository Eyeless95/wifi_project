from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from wifi.apps.dashboard.views import Dashboard, ajax_dashboard_datatable, add_advertisement, change_ad_state

app_name = 'dashboard'

urlpatterns = [
    url(r'^$', login_required(Dashboard.as_view()), name='dashboard'),
    url(r'^ajax_dashboard_datatable/$', login_required(ajax_dashboard_datatable), name='ajax_dashboard_datatable'),
    url(r'^add_advertisement/$', login_required(add_advertisement), name='add_advertisement'),
    url(r'^change_ad_state/$', login_required(change_ad_state), name='change_ad_state')
]
