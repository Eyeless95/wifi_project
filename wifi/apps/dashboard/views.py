import json
import traceback
import uuid

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from wifi.apps.dashboard.models import Advertisement, Statistic, UserSettings


class Dashboard(View):
    template_name = 'dashboard.html'

    def get(self, request):
        if request.user.is_superuser:
            data = {
                'users': User.objects.all().count(),
                'ads_count': Advertisement.objects.all().count(),
                'ads_views': Statistic.objects.all().aggregate(views=Sum('views'))['views'],
                'views_remain': UserSettings.objects.all().aggregate(views=Sum('views_remain'))['views'],
            }
        else:
            settings = UserSettings.objects.get(user=request.user)
            data = {
                'ads_count': Advertisement.objects.filter(user=request.user).count(),
                'ads_views': Statistic.objects.filter(advertisement__user=request.user).aggregate(
                    views=Sum('views'))['views'],
                'views_remain': settings.views_remain,
                'ads_allowed': settings.ads_remain
            }
        return render(request, self.template_name, context=data)


def ajax_dashboard_datatable(request):
    ajax_response = {'sEcho': '', 'aaData': [], 'iTotalRecords': 0, 'iTotalDisplayRecords': 0}
    start = int(request.GET.get('iDisplayStart', 0))
    length = int(request.GET.get('iDisplayLength', 0))
    ads = Advertisement.objects.filter(user=request.user)
    ajax_response['iTotalRecords'] = ads.count()
    ajax_response['iTotalDisplayRecords'] = ajax_response['iTotalRecords']
    for row in ads[start: start + length]:
        ajax_response['aaData'].append([row.name, row.ad_link, row.ad_statisic.views, '', row.enabled, row.id])
    return HttpResponse(json.dumps(ajax_response))


@csrf_exempt
def add_advertisement(request):
    ad_name = request.POST.get('ad_name', None)
    if ad_name in [None, '']:
        return HttpResponse(json.dumps({'status': False, 'reason': 'You did not specify name'}))
    file_path = request.FILES.get('file_path', None)
    if file_path in [None, '']:
        return HttpResponse(json.dumps({'status': False, 'reason': 'You did not upload file'}))
    fs = FileSystemStorage()
    filename = fs.save('{}.{}'.format(uuid.uuid4().hex, file_path.content_type.split('/')[1]), file_path)
    uploaded_file_url = fs.url(filename)
    adv = Advertisement.objects.create(user=request.user, name=ad_name, ad_link=uploaded_file_url)
    adv.create_ad_statistic()
    return HttpResponse(json.dumps({'status': True}))


@csrf_exempt
def change_ad_state(request):
    response = json.loads(request.POST.get('data', {}))
    ajax_response = {'status': False}
    try:
        ad = Advertisement.objects.get(id=response.get('id'))
        if response.get('action', '') == 'delete':
            ad.delete()
        else:
            ad.enabled = True if response.get('action', '') == 'show' else False
            ad.save()
        ajax_response['status'] = True
    except Exception:
        print(traceback.format_exc())
        pass
    return HttpResponse(json.dumps(ajax_response))
