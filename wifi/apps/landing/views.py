from django.shortcuts import render
from django.views import View


class Landing(View):
    template_name = 'landing.html'

    def get(self, request):
        return render(request=request, template_name=self.template_name)
