from django.shortcuts import render, redirect

from django.views import View
from django.views import generic

class khu_calendar(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'khu_calendar/index.html'
        return render(request, template_name)

# Create your views here.
