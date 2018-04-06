import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt


class Advertisement(View):
    template_name = 'advertisement.html'

    def get(self, request):
        return render(request, self.template_name)


class ThankYouPage(View):
    template_name = 'thank_you_page.html'

    def get(self, request):
        return render(request, self.template_name)


@csrf_exempt
def callback_and_redirect(request):
    return HttpResponse(json.dumps({'status': True}))
