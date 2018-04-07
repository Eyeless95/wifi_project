import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class Dashboard(View):
    template_name = 'dashboard.html'

    def get(self, request):
        return render(request, self.template_name)


def ajax_dashboard_datatable(request):
    ajax_response = {'sEcho': '', 'aaData': [], 'iTotalRecords': 0, 'iTotalDisplayRecords': 0}
    return HttpResponse(json.dumps(ajax_response))
