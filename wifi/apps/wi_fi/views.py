import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from wifi.apps.dashboard.models import UserSettings, Statistic, Advertisement as Ads


class Advertisement(View):
    template_name = 'advertisement.html'

    def get(self, request):
        ad = Ads.objects.filter(user__settings__views_remain__gt=0).order_by('?').first()
        if ad:
            stat = Statistic.objects.get(advertisement=ad)
            stat.views += 1
            stat.save()
            settings = UserSettings.objects.get(user=ad.user)
            settings.views_remain -= 1
            settings.save()
            data = {'ad': ad.ad_link}
        else:
            data = {'ad': '/media/default.jpg'}
        return render(request, self.template_name, context=data)


class ThankYouPage(View):
    template_name = 'thank_you_page.html'

    def get(self, request):
        return render(request, self.template_name)


@csrf_exempt
def callback_and_redirect(request):
    return HttpResponse(json.dumps({'status': True}))
